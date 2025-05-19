import os
import re
import datetime
import markdown as md
from bs4 import BeautifulSoup
from collections import defaultdict


# Dictionary to store plain text content by file path
plain_text_by_doc = defaultdict(list)


def on_page_markdown(markdown, page, config, files):

    # Split path: e.g. en/cr/chapter-1.md -> [en, cr, chapter-1.md]
    groups = re.match(r"^([a-z]+)/(.+)", page.file.src_uri)
    if groups:
        lang = config.get('theme', {}).get('language', 'en') # en, ja, etc.
        doc = page.meta.get('document')  # e.g. cr, trp, etc.
        cha = page.meta.get('chapter')  # e.g. 01-grame-concept.md, etc.

        # Only process files that are numbered
        if doc and cha:
            # Convert markdown -> html -> plain text
            html = md.markdown(markdown, extensions=['extra'])
            soup = BeautifulSoup(html, 'html.parser')
            plain_text = soup.get_text()

            # Store plain text by file parts (language, document)
            doc_key = f"{lang}-{doc}"
            plain_text_by_doc[doc_key].append((cha, plain_text))
    return markdown


def on_post_build(config):

    # Ensure the plain text directory exists
    plain_text_dir = os.path.join(config.site_dir, "..", "txt")
    os.makedirs(plain_text_dir, exist_ok=True)

    for doc_key, chapters in plain_text_by_doc.items():
        lang, doc = doc_key.split('-')
        version = config.extra.get(doc, {'version':'unknown'}).get('version', 'unknown')
        now = datetime.datetime.now()

        # Sort chapters by filename and combine text
        sorted_chapters = sorted(chapters, key=lambda x: x[0])
        combined_text = re.sub(r'\n+', '\n', '\n'.join(text for _, text in sorted_chapters))

        # Overwritse latest file if it exists
        # e.g. txt/latest/en-fab-cr.txt
        latest_dir = os.path.join(plain_text_dir, 'latest')
        os.makedirs(latest_dir, exist_ok=True)
        latest_path = os.path.join(latest_dir, f'{lang}-fab-{doc}.txt')
        with open(latest_path, "w", encoding="utf-8") as f:
            f.write(combined_text)

        # Create a unique file name with timestamp
        # e.g. txt/archive/en-fab-cr-2.10.1-20250505120000.txt
        unique_dir = os.path.join(plain_text_dir, "archive")
        os.makedirs(unique_dir, exist_ok=True)
        unique_path = os.path.join(unique_dir, f'{lang}-fab-{doc}-{version}-{now:%Y%m%d%H%M%S}.txt')
        with open(unique_path, "w", encoding="utf-8") as f:
            f.write(combined_text)
    
    # Clear after processing to avoid duplicate data when doing multiple languages
    plain_text_by_doc.clear()

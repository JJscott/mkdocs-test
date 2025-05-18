rules_data = {}

import os
import re
import markdown as md
from bs4 import BeautifulSoup
from collections import defaultdict

# Dictionary to store plain text content by file path
plain_text_by_doc = defaultdict(list)


def on_page_markdown(markdown, page, config, files):

    # Split path: e.g. en/cr/chapter-1.md -> [en, cr, chapter-1.md]
    groups = re.match(r"^([a-z]{2})/([^/]+)/(.+)", page.file.src_uri)
    if groups:
        lang = groups.group(1)  # e.g. en, ja
        doc = groups.group(2)  # e.g. cr, trp, etc.
        file = groups.group(3)  # e.g. 01-grame-concept.md, etc.

        # Only process files that start with a chapter number
        match = re.match(r"^\d{2}-.*\.md$", file)
        if match:
            # Convert to plain text from the markdown
            html = md.markdown(markdown, extensions=['extra'])
            soup = BeautifulSoup(html, 'html.parser')
            plain_text = soup.get_text()

            # Store plain text by file parts (language, document)
            doc_key = f"{lang}-{doc}"
            plain_text_by_doc[doc_key].append((file, plain_text))
    return markdown


def on_post_build(config):
    plain_text_dir = os.path.join(config.site_dir, "plain_text")
    os.makedirs(plain_text_dir, exist_ok=True)

    # We assume that list is in alphbetical order
    for doc_key, chapters in plain_text_by_doc.items():
        lang, doc = doc_key.split('-')

        # Sort chapters by filename
        sorted_chapters = sorted(chapters, key=lambda x: x[0])
        combined_text = re.sub(r'\n+', '\n', '\n'.join(text for _, text in sorted_chapters))

        output_dir = os.path.join(plain_text_dir, lang, doc)
        os.makedirs(output_dir, exist_ok=True)
        output_path = os.path.join(output_dir, "raw.txt")

        with open(output_path, "w", encoding="utf-8") as f:
            f.write(combined_text)
        print(f"Written plain text to {output_path}")
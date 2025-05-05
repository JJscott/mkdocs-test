# rules_data = {}


# import os
# import re
# import markdown
# from bs4 import BeautifulSoup

# # Dictionary to store plain text content by file path
# plain_text_by_path = {}

# def strip_markdown_to_text(markdown_content):
#     # Convert markdown to HTML, then extract plain text using BeautifulSoup
#     html = markdown.markdown(markdown_content, extensions=['extra'])
#     soup = BeautifulSoup(html, 'html.parser')
#     return soup.get_text()

# def on_page_markdown(markdown, page, config, files):
#     # Convert and store the plain text version for this page
#     plain_text = strip_markdown_to_text(markdown)
#     plain_text_by_path[page.file.src_path] = plain_text
#     return markdown

# def on_post_build(config):
#     output_dir = os.path.join(config.site_dir, "plain_text")
#     os.makedirs(output_dir, exist_ok=True)

#     for src_path, text in plain_text_by_path.items():
#         # Generate corresponding output path
#         name = os.path.splitext(os.path.basename(src_path))[0]
#         txt_path = os.path.join(output_dir, f"{name}.txt")

#         # Save plain text to .txt file
#         with open(txt_path, "w", encoding="utf-8") as f:
#             f.write(text)

# def on_page_markdown(self, markdown, page, config, files):
#     rules = []
#     current_rule = None

#     for line in markdown.split("\n"):
#         if line.startswith("#"):  # Header lines
#             if current_rule:
#                 rules.append(current_rule)
#             current_rule = {"number": "", "title": line.strip("# ").strip(), "content": "", "id": page.url}
#         elif current_rule:
#             current_rule["content"] += line.strip() + " "

#     if current_rule:
#         rules.append(current_rule)

#     self.rules_data[page.url] = rules
#     return markdown  # Return unmodified Markdown

# def on_page_markdown(self, markdown, page, config, files):
#     rules = []
#     current_rule = None

#     for line in markdown.split("\n"):
#         if line.startswith("#"):  # Header lines
#             if current_rule:
#                 rules.append(current_rule)
#             current_rule = {"number": "", "title": line.strip("# ").strip(), "content": "", "id": page.url}
#         elif current_rule:
#             current_rule["content"] += line.strip() + " "

#     if current_rule:
#         rules.append(current_rule)

#     self.rules_data[page.url] = rules
#     return markdown  # Return unmodified Markdown

# def on_post_build(self, config):
#     output_path = os.path.join(config['site_dir'], "rules.json")
#     with open(output_path, "w", encoding="utf-8") as f:
#         json.dump(self.rules_data, f, indent=2)
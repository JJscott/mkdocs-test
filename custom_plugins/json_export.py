import os
import json
import mkdocs.plugins
from mkdocs.structure.pages import Page

class JSONExportPlugin(mkdocs.plugins.BasePlugin):
    rules_data = {}

    def on_page_markdown(self, markdown: str, page: Page, config, files):
        """Extract rules and store them for JSON output"""
        rules = []
        current_rule = None

        for line in markdown.split("\n"):
            if line.startswith("#"):  # Header lines
                if current_rule:
                    rules.append(current_rule)
                current_rule = {"number": "", "title": line.strip("# ").strip(), "content": "", "id": page.url}
            elif current_rule:
                current_rule["content"] += line.strip() + " "

        if current_rule:
            rules.append(current_rule)

        self.rules_data[page.url] = rules
        return markdown  # Return unmodified Markdown

    def on_post_build(self, config):
        """Save extracted rules as JSON"""
        output_path = os.path.join(config['site_dir'], "rules.json")
        with open(output_path, "w", encoding="utf-8") as f:
            json.dump(self.rules_data, f, indent=2)
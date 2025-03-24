import re

# label_map = {}  # Stores { "label": "1.2.3." } mappings

reference_flag_regex = r"\[REF book=([A-Z]+) chap=(\d+)\]"
label_re = r"@@((cha|sec|rule):\w+)@@" # e.g. @@rule:label@@
ref_re = r"\[\[((cha|sec|rule):\w+)\]\]" # e.g. [[rule:label]]


def process_references(markdown, process_rule):
    """
    Runs process_rule function once for each rule in the markdown.
    """
    match = re.match(reference_flag_regex, markdown)
    if match:
        rulebook, chapter = match.groups()

        # Track numbering. Sections always start with 0 (e.g. 1.0 General)
        # Numbering starts with -1 to account for the first increment
        numbering = [int(chapter)-1, -1, 0, 0]
        lines = markdown.split("\n")
        
        for line in lines:
            match = re.match(r"^(#{1,4})\s*(.*)", line)
            if match:
                hashes, text = match.groups()
                header_level = len(hashes)

                # Calulate rule number and increase numbering
                # Chapter, section, rule, subrule (e.g. 1, 1.2, 1.2.3, 1.2.3d)
                numbering[header_level-1] += 1
                rule_number = ".".join(map(str, numbering[:header_level]))
                if header_level == 1:
                    numbering[1:] = [-1, 0, 0]
                elif header_level == 2:
                    numbering[2:] = [0, 0]
                elif header_level == 3:
                    numbering[3] = 0
                else:
                    letter_suffix = chr(96 + numbering[3]) # number -> letter
                    rule_number = ".".join(map(str, numbering[:3])) + letter_suffix

                # Create anchor from rule number
                anchor = f'{rulebook}{rule_number}'


                # Call function to process the rule
                # - Record label-anchor mappings OR
                # - Remove labels from text and replace references with anchors
                process_rule(text, hashes, rule_number, anchor)
            else:
                process_rule(line)

def on_files(files, config):
    """
    Process each Markdown page before rendering.
    - Initialize global label mapping
    - Record labels and anchors
    """

    # Initialize global label mapping
    if "label_map" not in config.extra:
        config.extra["label_map"] = {}

    base_url = config.site_url.rstrip('/') if "site_url" in config else ""

    for file in files:
        if file.is_documentation_page():
            markdown = file.content_string

            def record_label(text, hashes=None, rule_number=None, anchor=None):
                if hashes:
                    label_match = re.search(label_re, text)
                    if label_match:
                        label = label_match.group(1)
                        url = f"{base_url}/{file.url}"
                        config.extra["label_map"][label] = (rule_number, anchor, url)

            process_references(markdown, record_label)

    return files





def on_page_markdown(markdown, page, config, files, **kwargs):
    """
    Process each Markdown page before rendering.
    - Replace references with hyperlinks
    - Insert rule numbers and anchors
    """

    # Replace references with hyperlinks
    def replace_reference(match):
        label = match.group(1)
        if label in config.extra["label_map"]:
            rule_number, anchor, url = config.extra["label_map"][label]
            return f"<sup>[\[{rule_number}\]]({url}#{anchor})</sup>"
        return f"<sup>[\[{label}\]]({label})</sup>"


    markdown = re.sub(ref_re, replace_reference, markdown)


    # Check if we're processing labels
    match = re.match(reference_flag_regex, markdown)
    if not match:
        return markdown


    # Insert rule numbers and anchors
    processed = []
    def remove_label(text, hashes=None, rule_number=None, anchor=None):
        if hashes:
            label_match = re.search(label_re, text)
            if label_match:
                text = text.replace(label_match.group(0), "").strip()
            numbered_heading = f"{hashes} {rule_number} {text} {{ #{anchor} }}"
            processed.append(numbered_heading)
            
        else:
            processed.append(text)

    process_references(markdown, remove_label)
    markdown = "\n".join(processed)

    # Finally, remove the reference flag
    markdown = re.sub(reference_flag_regex, "", markdown)


    return markdown





    

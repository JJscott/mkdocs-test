import re

icon_label ={
    "d": "Defense",
    "u": "Untap",
    "t": "Tap",
    "c": "Chi",
    "h": "Life",
    "p": "Power",
    "i": "Intellect",
    "r": "Resource"
}

def on_post_page(output, page, config):
    base_url = config.site_url.rstrip('/') if "site_url" in config else ""

    def replacer(match):
        key = match.group(1)
        label = icon_label.get(key, "unknown")
        return f'<span class="inline-icon"><img src="{base_url}/assets/images/icon_{key}.png" title="{label}" alt="{{{key}}}" aria-label=" {label}"></span>'

    return re.sub(r"\{([dutchpir])\}", replacer, output)
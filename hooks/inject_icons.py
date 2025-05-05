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
    def replacer(match):
        key = match.group(1)
        label = icon_label.get(key, "unknown")
        return f'<span class="inline-icon"><img src="{config.site_url}/assets/images/icon_{key}.png" title="{label}" alt="{{{key}}}" aria-label=" {label}"></span>'

    return re.sub(r"\{([dutchpir])\}", replacer, output)
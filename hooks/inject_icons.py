import re

def on_post_page(output, page, config):
    return re.sub(r"\{([dutchpir])\}", f'<span class="inline-icon"><img src="{config.site_url}/assets/images/icon_\\1.webp" alt="{{\\1}}"></span>', output)
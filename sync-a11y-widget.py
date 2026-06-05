import re
index = open('index.html', encoding='utf-8').read()
widget = open('partials/a11y-widget.html', encoding='utf-8').read()

# Replace inline widget block
index = re.sub(
    r'  <!-- Smart Accessibility widget -->.*?</div>\s*\n\s*<style>\s*\[x-sa-cloak\]',
    '  <!-- Smart Accessibility widget -->\n' + widget + '\n  <style>\n    [x-sa-cloak]',
    index,
    count=1,
    flags=re.DOTALL
)

# Move a11y scripts to head (remove from footer duplicate)
footer_block = re.search(
    r'\s*<script>window\.sa_shop_domain.*?</script>\s*<script src="js/a11y-settings\.js"></script>\s*<script src="https://cdn\.shopify\.com/extensions/019d9b3d-db05-79e1-ad33-4ab8d9a31d79/smart-accessibility-1-24/assets/sa-widget\.js" defer></script>\s*',
    index,
    re.DOTALL
)
if footer_block:
    index = index[:footer_block.start()] + '\n' + index[footer_block.end():]

head_insert = '''  <link rel="stylesheet" href="css/a11y-support.css">
  <script>window.sa_shop_domain = 'shopjerseybird.myshopify.com';</script>
  <script src="js/a11y-settings.js"></script>
  <script src="https://cdn.shopify.com/extensions/019d9b3d-db05-79e1-ad33-4ab8d9a31d79/smart-accessibility-1-24/assets/sa-widget.js" defer></script>
'''
if 'css/a11y-support.css' not in index:
    index = index.replace(
        '  <link rel="stylesheet" href="https://cdn.shopify.com/extensions/019d9b3d-db05-79e1-ad33-4ab8d9a31d79/smart-accessibility-1-24/assets/sa-widget.css">\n</head>',
        '  <link rel="stylesheet" href="https://cdn.shopify.com/extensions/019d9b3d-db05-79e1-ad33-4ab8d9a31d79/smart-accessibility-1-24/assets/sa-widget.css">\n' + head_insert + '</head>'
    )

open('index.html', 'w', encoding='utf-8').write(index)
print('synced')

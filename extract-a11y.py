import re
html = open('ref-page.html', encoding='utf-8', errors='ignore').read()
# Settings script
m = re.search(r'(window\.sa_settings_from_metafield\s*=\s*\{.*?\};\s*)', html, re.DOTALL)
settings = m.group(1) if m else ''
settings = settings.replace('JerseyBird Accessibility', 'Accessibility')
settings = settings.replace('JerseyBird Smart Accessibility App', 'Smart Accessibility App')
settings = settings.replace('At JerseyBird, we', 'We')
settings = settings.replace('jerseybird.com', 'this website')
open('js/a11y-settings.js', 'w', encoding='utf-8').write(settings + '\n')

start = html.find('class="smart-accessibility-widget ')
if start < 0:
    raise SystemExit('widget not found')
start = html.rfind('<div', 0, start)
depth = 0
i = start
end = len(html)
while i < len(html):
    if html.startswith('<div', i):
        depth += 1
        i += 4
        continue
    if html.startswith('</div>', i):
        depth -= 1
        i += 6
        if depth == 0:
            end = i
            break
        continue
    i += 1

widget = html[start:end]
widget = widget.replace('style="display: none;"', '')
widget = re.sub(r'\s*x-sa-cloak\s*', '\n', widget)
widget = widget.replace('data-shop="local"', 'data-shop="shopjerseybird.myshopify.com"')
import os
os.makedirs('partials', exist_ok=True)
open('partials/a11y-widget.html', 'w', encoding='utf-8').write(widget + '\n')
print('written', len(widget), 'chars')

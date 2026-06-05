import re
import html as html_lib
html = open('ref-page.html', encoding='utf-8', errors='ignore').read()
start = html.find('id="CurrencyList-toolbar"')
end = html.find('</ul>', start)
block = html[start:end]
items = re.findall(
    r'data-value="([A-Z]{2})".*?currency-flag--([a-z]{2})".*?disclosure-list__label">\s*([^<]+?)\s*</span>',
    block, re.DOTALL
)
seen = set()
out = []
for code, flag, label in items:
    label = html_lib.unescape(' '.join(label.split()))
    if code not in seen:
        seen.add(code)
        out.append({'code': code, 'flag': flag, 'label': label})

lines = ['/* Auto-extracted from JerseyBird */', 'const CURRENCIES = [']
for i, c in enumerate(out):
    comma = ',' if i < len(out) - 1 else ''
    label = c['label'].replace("'", "\\'")
    lines.append(f"  {{ code: '{c['code']}', flag: '{c['flag']}', label: '{label}' }}{comma}")
lines.append('];')
open('js/currencies.js', 'w', encoding='utf-8').write('\n'.join(lines) + '\n')
print(len(out), 'currencies written')

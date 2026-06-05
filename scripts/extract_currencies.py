import re
import json
from pathlib import Path

html = Path(__file__).parent.parent / "ref-page.html"
text = html.read_text(encoding="utf-8", errors="ignore")

block_re = re.compile(
    r'<li class="disclosure-list__item">\s*'
    r'<a class="disclosure-list__option"[^>]*data-value="([A-Z]{2})"[^>]*>'
    r'.*?currency-flag--([a-z]{2})".*?'
    r'<span class="disclosure-list__label">\s*(.*?)\s*</span>',
    re.S,
)

items = []
seen = set()
for m in block_re.finditer(text):
    code, flag, label = m.group(1), m.group(2), re.sub(r"\s+", " ", m.group(3)).strip()
    if code in seen:
        continue
    seen.add(code)
    items.append({"code": code, "flag": flag, "label": label})

out = Path(__file__).parent.parent / "js" / "currencies.js"
lines = [
    "/** Auto-generated from ref-page.html — %d countries */" % len(items),
    "window.JB_CURRENCIES = " + json.dumps(items, ensure_ascii=False, indent=2) + ";",
]
out.write_text("\n".join(lines), encoding="utf-8")
print("Wrote %d countries to %s" % (len(items), out))

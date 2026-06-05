"""Extract main page content from downloaded JerseyBird ref HTML."""
import re
import os

ROOT = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(ROOT, 'content')
os.makedirs(OUT, exist_ok=True)

PAGES = [
    ('ref-faqs1.html', 'faqs.html', 'FAQs'),
    ('ref-shipping-policy.html', 'shipping-policy.html', 'Shipping Policy'),
    ('ref-shipping-returns-faqs.html', 'returns-policy.html', 'Returns & Refunds Policy'),
    ('ref-terms-and-conditions.html', 'terms.html', 'Terms and Conditions'),
]


def strip_links(html):
    html = re.sub(r'href="https?://jerseybird\.com/products/[^"]*"', 'href="shop.html"', html)
    html = re.sub(r'href="https?://jerseybird\.com/pages/contact-us[^"]*"', 'href="contact.html"', html)
    html = re.sub(r'href="https?://jerseybird\.com[^"]*"', 'href="index.html"', html)
    html = re.sub(r'href="/search"', 'href="search.html"', html)
    html = re.sub(r'href="/pages/contact-us[^"]*"', 'href="contact.html"', html)
    html = re.sub(r'href="/"', 'href="index.html"', html)
    html = re.sub(r'target="_blank"', '', html)
    html = re.sub(r'data-id="[^"]*"', '', html)
    html = re.sub(r'<div class="title-desc">.*?</div>', '', html, flags=re.DOTALL)
    html = re.sub(r'<br\s*/?>\s*<br\s*/?>', '<br>', html)
    return html


def extract_rte(path):
    text = open(path, encoding='utf-8', errors='replace').read()
    m = re.search(
        r'<header class="section-header">.*?<h1[^>]*>(.*?)</h1>.*?</header>(.*?)'
        r'(?:</section>|<script data-locksmith)',
        text,
        re.DOTALL | re.IGNORECASE,
    )
    if not m:
        return None, None
    title = re.sub(r'<[^>]+>', '', m.group(1)).strip()
    body = m.group(2).strip()
    # Prefer full rte--nomargin wrapper content
    wrap = re.search(r'<div class="rte rte--nomargin">(.*)</div>\s*</div>\s*(?:</section>|</div>)', body, re.DOTALL)
    if wrap:
        inner = wrap.group(1).strip()
    else:
        blocks = re.findall(r'<div class="rte[^"]*">(.*?)</div>', body, re.DOTALL)
        inner = '\n'.join(blocks) if blocks else body
    inner = strip_links(inner)
    inner = re.sub(r'\n{3,}', '\n\n', inner)
    return title, inner


def extract_privacy(path):
    text = open(path, encoding='utf-8', errors='replace').read()
    m = re.search(
        r'shopify-policy__body.*?<div class="rte">(.*)</div>\s*</div>\s*</div>\s*<script',
        text,
        re.DOTALL | re.IGNORECASE,
    )
    if not m:
        return None, None
    inner = strip_links(m.group(1).strip())
    return 'Privacy policy', inner


ref_priv = os.path.join(ROOT, 'ref-privacy-policy.html')
if os.path.isfile(ref_priv):
    title, inner = extract_privacy(ref_priv)
    if inner:
        frag = f'<div class="rte rte--nomargin shopify-policy__rte">\n{inner}\n</div>'
        open(os.path.join(OUT, 'privacy.fragment.html'), 'w', encoding='utf-8').write(frag)
        print('ok privacy.html', title)

for ref, out, default_title in PAGES:
    ref_path = os.path.join(ROOT, ref)
    if not os.path.isfile(ref_path):
        print('skip missing', ref)
        continue
    title, inner = extract_rte(ref_path)
    if not inner:
        print('no content', ref)
        continue
    title = title or default_title
    frag = f'<div class="rte rte--nomargin">\n{inner}\n</div>'
    open(os.path.join(OUT, out.replace('.html', '.fragment.html')), 'w', encoding='utf-8').write(frag)
    print('ok', out, title[:40])

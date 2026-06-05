import re, html, pathlib
files = [
  "ref-faqs1.html","ref-shipping-policy.html","ref-shipping-returns-faqs.html",
  "ref-terms-and-conditions.html","ref-privacy-policy.html","ref-ambassador-application.html",
  "ref-pro-series.html","ref-search.html",
]
def strip_tags(s):
    s = re.sub(r"<script[\s\S]*?</script>", " ", s, flags=re.I)
    s = re.sub(r"<style[\s\S]*?</style>", " ", s, flags=re.I)
    s = re.sub(r"<[^>]+>", " ", s)
    s = html.unescape(s)
    return re.sub(r"\s+", " ", s).strip()

for fn in files:
    p = pathlib.Path(fn)
    if not p.exists():
        print("MISSING", fn)
        continue
    raw = p.read_text(encoding="utf-8", errors="replace")
    og = re.search(r'property="og:title"\s+content="([^"]+)"', raw)
    page_title = og.group(1) if og else ""
    if not page_title:
        for t in re.findall(r"<title>([^<]+)</title>", raw, re.I):
            if len(t) > 5 and "icon" not in t.lower():
                page_title = t
                break
    h1m = re.search(r'<h1[^>]*class="section-header__title"[^>]*>([\s\S]*?)</h1>', raw, re.I)
    if not h1m:
        h1m = re.search(r"<h1[^>]*>([\s\S]*?)</h1>", raw, re.I)
    h1 = strip_tags(h1m.group(1)) if h1m else ""
    idx = raw.find('class="rte"')
    if idx == -1:
        idx = raw.find("rte setting")
    rte = raw[idx : idx + 150000] if idx != -1 else raw[2000:100000]
    heads = []
    for hm in re.finditer(r"<h([2-4])[^>]*>([\s\S]*?)</h\1>", rte, re.I):
        heads.append((int(hm.group(1)), strip_tags(hm.group(2))[:150]))
    paras = re.findall(r"<p[^>]*>([\s\S]*?)</p>", rte, re.I)
    sections = []
    for lvl, title in heads[:20]:
        fp = ""
        pos = rte.lower().find(title.lower()[:40]) if title else -1
        if pos > 0:
            sub = rte[pos : pos + 4000]
            pm = re.search(r"<p[^>]*>([\s\S]*?)</p>", sub, re.I)
            if pm:
                fp = strip_tags(pm.group(1))[:220]
        sections.append((lvl, title, fp))
    mobile = sorted(set(re.findall(r"\b(?:small--|medium--|large--)[a-zA-Z0-9_-]+", raw)))
    hide_show = sorted(set(re.findall(r"\b(?:hide|show)-[a-zA-Z0-9_-]+", raw)))[:12]
    canonical = re.search(r'rel="canonical"\s+href="([^"]+)"', raw)
    print("\n" + "=" * 60)
    print(fn, p.stat().st_size)
    if canonical:
        print("canonical:", canonical.group(1))
    print("page_title:", page_title)
    print("h1:", h1)
    for lvl, title, fp in sections[:10]:
        print(f"  h{lvl}: {title}")
        if fp:
            print(f"       -> {fp[:200]}")
    if not sections and paras:
        print("  (no h2-h4) first_p:", strip_tags(paras[0])[:220])
    print("mobile:", ", ".join(mobile[:12]))
    if hide_show:
        print("hide/show:", ", ".join(hide_show[:8]))

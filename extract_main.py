import re, html, pathlib

def strip_tags(s):
    s = re.sub(r"<script[\s\S]*?</script>", " ", s, flags=re.I)
    s = re.sub(r"<[^>]+>", " ", s)
    s = html.unescape(s)
    return re.sub(r"\s+", " ", s).strip()

files = [
  ("ref-faqs1.html", "faqs.md"),
  ("ref-shipping-policy.html", "shipping-policy.md"),
  ("ref-shipping-returns-faqs.html", "shipping-returns-faqs.md"),
  ("ref-terms-and-conditions.html", "terms-and-conditions.md"),
  ("ref-privacy-policy.html", "privacy-policy.md"),
  ("ref-ambassador-application.html", "ambassador-application.md"),
  ("ref-pro-series.html", "pro-series.md"),
  ("ref-search.html", "search.md"),
]

for fn, outname in files:
    raw = pathlib.Path(fn).read_text(encoding="utf-8", errors="replace")
    m = re.search(r'<main[^>]*id="MainContent"[^>]*>([\s\S]*?)</main>', raw, re.I)
    main = m.group(1) if m else raw
    og = re.search(r'property="og:title"\s+content="([^"]+)"', raw)
    page_title = html.unescape(og.group(1)) if og else ""
    h1m = re.search(r'section-header__title"[^>]*>([\s\S]*?)</h1>', main, re.I)
    h1 = strip_tags(h1m.group(1)) if h1m else ""
    rtes = re.findall(r'<div class="rte[^"]*">([\s\S]*?)</div>', main, re.I)
    body = "\n".join(rtes) if rtes else main
    heads = []
    for tag in ("h2", "h3", "h4", "strong"):
        for hm in re.finditer(rf"<{tag}[^>]*>([\s\S]*?)</{tag}>", body, re.I):
            t = strip_tags(hm.group(1))
            if t and t.lower() != "currency" and len(t) > 1:
                heads.append((tag, t[:140]))
    paras = [strip_tags(p) for p in re.findall(r"<p[^>]*>([\s\S]*?)</p>", body, re.I)]
    paras = [p for p in paras if len(p) > 30][:8]
    details = re.findall(r"<details[^>]*>[\s\S]*?<summary[^>]*>([\s\S]*?)</summary>", body, re.I)
    summaries = [strip_tags(s)[:120] for s in details[:10]]
    layout = []
    for pat in [r'page-width--narrow', r'page-content', r'section-header', r'template-page', r'small--hide', r'medium-up--', r'grid__item', r'collapsible', r'accordion']:
        if re.search(pat, raw, re.I):
            layout.append(pat.replace(r'\\', ''))
    lines = [f"# {page_title or h1}", f"**Local file:** `{outname}`", f"**Source:** `{fn}`", "", f"**H1:** {h1}", ""]
    if summaries:
        lines += ["## FAQ / accordion items", *[f"- {s}" for s in summaries], ""]
    if heads:
        lines += ["## Headings in main RTE", *[f"- ({t}) {h}" for t,h in heads[:15]], ""]
    if paras:
        lines += ["## Key paragraphs", *[f"- {p[:300]}" for p in paras[:5]], ""]
    lines += ["## Layout / mobile classes", f"- Wrapper: `main#main-content` > `page-width page-width--narrow page-content` > `section-header` + `rte`", f"- Body: `template-page`", f"- Mobile-related in full page: `small--hide` (footer/currency drawer); a11y `hide-buy-now`, `hide-images`", f"- Patterns found: {', '.join(sorted(set(layout)))}", ""]
    pathlib.Path("summaries").mkdir(exist_ok=True)
    pathlib.Path("summaries") / outname
    (pathlib.Path("summaries") / outname).write_text("\n".join(lines), encoding="utf-8")
    print(fn, "->", outname, "rte_blocks", len(rtes), "headings", len(heads), "paras", len(paras), "details", len(summaries))

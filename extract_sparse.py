import re,html,pathlib
for fn in ["ref-shipping-returns-faqs.html","ref-ambassador-application.html","ref-pro-series.html","ref-search.html"]:
 raw=pathlib.Path(fn).read_text(encoding="utf-8",errors="replace")
 m=re.search(r"<main[^>]*id=.MainContent.[^>]*>([\s\S]*?)</main>",raw,re.I)
 main=m.group(1) if m else ""
 print("===",fn)
 print("body class snippet:", re.search(r"<body[^>]*class=\"([^\"]+)\"", raw,re.I).group(1)[:80] if re.search(r"<body[^>]*class=\"([^\"]+)\"", raw,re.I) else "")
 for pat in ["rte","iframe","typeform","search-bar","template-search","predictive-search","page-content"]:
  print(pat, main.lower().count(pat.lower()))
 rtes=re.findall(r"<div class=\"rte[^\"]*\">([\s\S]*?)</div>",main,re.I)
 for i,b in enumerate(rtes):
  t=re.sub(r"<[^>]+>"," ",b); t=html.unescape(re.sub(r"\s+"," ",t).strip())
  if t: print("rte",i,":",t[:600])
 # non-rte main chunks
 if not rtes:
  chunk=main[0:8000]
  t=re.sub(r"<[^>]+>"," ",chunk); t=html.unescape(re.sub(r"\s+"," ",t).strip())
  print("main text sample:", t[:700])

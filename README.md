# Local project site

Same layout as the reference design. All pages work on **localhost** (no JerseyBird external links).

## Run locally

```bash
cd form
python -m http.server 8765
```

Open in browser:

- http://localhost:8765/index.html — Start a project (form)
- http://localhost:8765/login.html — Log in
- http://localhost:8765/signup.html — Sign up
- http://localhost:8765/shop.html — Shop
- http://localhost:8765/about.html — About
- http://localhost:8765/contact.html — Contact
- http://localhost:8765/search.html — Search
- http://localhost:8765/faqs.html — FAQs
- http://localhost:8765/shipping-policy.html — Shipping Policy
- http://localhost:8765/returns-policy.html — Returns & Refunds
- http://localhost:8765/terms.html — Terms of Service
- http://localhost:8765/privacy.html — Privacy Policy
- http://localhost:8765/ambassador.html — Ambassador Application
- http://localhost:8765/pro-series.html — Pro Series

## Navbar

- **Shop** → `shop.html` (separate icon in header)
- **Cart** → opens cart drawer (separate button, spaced from shop)
- **Log in** → `login.html`
- **Currency** → dropdown with all countries (saved in browser)

## Rebuild pages after editing `partials/shell.html`

```bash
python build-shell.py
python build-all-pages.py
```

## Refresh footer/policy page text from JerseyBird HTML

If `ref-*.html` files exist in the project folder:

```bash
python extract-page-content.py
python build-all-pages.py
```

## Footer pages (all match live site layout)

| Footer link | File | Same as live |
|-------------|------|----------------|
| Home Page | `index.html` | Start a Project (Paperform) |
| Search | `search.html` | Search bar + product grid |
| Contact Us | `contact.html` | Get in touch form |
| Become an Ambassador | `ambassador.html` | Paperform embed |
| FAQs | `faqs.html` | Full FAQ text |
| Shipping Policy | `shipping-policy.html` | Policy text |
| Returns & Refunds | `returns-policy.html` | Policy + bullet list |
| Terms of Service | `terms.html` | Full terms |
| Privacy Policy | `privacy.html` | Full privacy policy |
| JerseyBird Pro Series | `pro-series.html` | Black page + Paperform |

import re
path = 'index.html'
html = open(path, encoding='utf-8').read()

# Remove external JerseyBird / app links (keep design, local navigation)
html = re.sub(r'https://jerseybird\.com[^"\s]*', '#', html)
html = re.sub(r'https://app\.jerseybird\.com[^"\s]*', '#', html)
html = re.sub(r'https://www\.instagram\.com/jerseybirdofficial/', '#', html)
html = re.sub(r'https://www\.facebook\.com/search/top\?q=jerseybird%20official', '#', html)
html = re.sub(r'https://twitter\.com/JerseyBirdShop', '#', html)
html = re.sub(r'https://www\.tiktok\.com/@jerseybirdofficial', '#', html)

# Logo home -> local
html = html.replace('href="#" class="site-header__logo-link"', 'href="index.html" class="site-header__logo-link"')
html = html.replace('<title>START A PROJECT – JerseyBird</title>', '<title>START A PROJECT</title>')

# Login: same-page handler, not external
html = html.replace(
    '<a href="#" class="site-nav__link site-nav__link--icon small--hide" aria-label="Log in">',
    '<button type="button" class="site-nav__link site-nav__link--icon small--hide js-login-open" aria-label="Log in">'
)
html = html.replace(
    '</svg>\n            </a>\n            <button type="button" class="site-nav__link site-nav__link--icon js-cart-open"',
    '</svg>\n            </button>\n            <button type="button" class="site-nav__link site-nav__link--icon js-cart-open"',
    1
)
html = html.replace('<li class="mobile-nav__item"><a href="#" class="mobile-nav__link">Log in</a></li>',
    '<li class="mobile-nav__item"><button type="button" class="mobile-nav__link js-login-open">Log in</button></li>')

# Search form local
html = html.replace(
    '<form class="site-header__search-form" action="#" method="get">',
    '<form class="site-header__search-form" action="#" method="get" id="headerSearchForm">'
)

# Replace old a11y block with Smart Accessibility (JerseyBird widget)
a11y_old = re.search(r'\s*<!-- Accessibility widget -->.*?</div>\s*\n\s*<script src="js/currencies.js">', html, re.DOTALL)
widget = open('partials/a11y-widget.html', encoding='utf-8').read()
a11y_new = '''
  <!-- Smart Accessibility widget (same as jerseybird.com) -->
  <link rel="stylesheet" href="https://cdn.shopify.com/extensions/019d9b3d-db05-79e1-ad33-4ab8d9a31d79/smart-accessibility-1-24/assets/sa-widget.css">
''' + widget + '''
  <script src="js/a11y-settings.js"></script>
  <script src="https://cdn.shopify.com/extensions/019d9b3d-db05-79e1-ad33-4ab8d9a31d79/smart-accessibility-1-24/assets/sa-widget.js" defer></script>

  <script src="js/currencies.js">'''

if a11y_old:
    html = html[:a11y_old.start()] + a11y_new + html[a11y_old.end():]
else:
    print('WARN: a11y block not found')

# Login drawer before cart overlay end? Insert after cart drawer
login_drawer = '''
  <!-- Login panel (local, matches site flow) -->
  <div id="LoginDrawer" class="drawer drawer--right drawer--narrow" aria-hidden="true">
    <div class="drawer__contents">
      <div class="drawer__fixed-header">
        <div class="drawer__header">
          <h2 class="drawer__title">Log in</h2>
          <button type="button" class="drawer__close-button js-login-close" aria-label="Close">
            <svg class="icon icon-close" viewBox="0 0 64 64" aria-hidden="true"><path d="M19 17.61l27.12 27.13m0-27.12L19 44.74"/></svg>
          </button>
        </div>
      </div>
      <div class="drawer__inner">
        <div class="drawer__scrollable login-drawer__body">
          <p class="login-drawer__hint">Sign in to your account to view orders and saved projects.</p>
          <form class="login-drawer__form" id="loginForm">
            <label class="login-drawer__label">Email<input type="email" name="email" required autocomplete="email"></label>
            <label class="login-drawer__label">Password<input type="password" name="password" required autocomplete="current-password"></label>
            <button type="submit" class="btn btn--checkout btn--login">Log in</button>
          </form>
          <p class="login-drawer__footer"><a href="#">Forgot password?</a> · <a href="#">Create account</a></p>
        </div>
      </div>
    </div>
  </div>

'''
if 'id="LoginDrawer"' not in html:
    html = html.replace('<div class="drawer-overlay js-drawer-close"', login_drawer + '<div class="drawer-overlay js-drawer-close"', 1)

open(path, 'w', encoding='utf-8').write(html)
print('index.html patched')

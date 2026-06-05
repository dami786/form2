"""Build partials/shell.html from index with local links and generic labels."""
import re
html = open('index.html', encoding='utf-8').read()
start = html.find('<a class="skip-link"')
end = html.find('<main class="main-content"')
shell = html[start:end]

replacements = [
    ('JerseyBird Project Portal login', 'Project Portal login'),
    ('What is JerseyBird?', 'About us'),
    ('JERSEYBIRD ON TOUR', 'ON TOUR'),
    ('JerseyBird Apparel', 'Apparel'),
    ('JerseyBird Night 2025', 'Night 2025'),
    ('JerseyBird Pro Series', 'Pro Series'),
    ('alt="JerseyBird"', 'alt="Logo"'),
    ('href="#" class="mobile-nav__sublist-link">Project Portal login', 'href="login.html" class="mobile-nav__sublist-link">Project Portal login'),
    ('href="#" class="site-nav__dropdown-link">Project Portal login', 'href="login.html" class="site-nav__dropdown-link">Project Portal login'),
    ('href="#" class="mobile-nav__sublist-link">About us', 'href="about.html" class="mobile-nav__sublist-link">About us'),
    ('href="#" class="site-nav__dropdown-link">About us', 'href="about.html" class="site-nav__dropdown-link">About us'),
    ('href="#" class="mobile-nav__sublist-link">Contact us', 'href="contact.html" class="mobile-nav__sublist-link">Contact us'),
    ('href="#" class="site-nav__dropdown-link">Contact us', 'href="contact.html" class="site-nav__dropdown-link">Contact us'),
    ('href="#" class="mobile-nav__link mobile-nav__link--top-level">ON TOUR', 'href="about.html" class="mobile-nav__link mobile-nav__link--top-level">ON TOUR'),
    ('href="#" class="site-nav__link site-nav__link--underline">ON TOUR', 'href="about.html" class="site-nav__link site-nav__link--underline">ON TOUR'),
    ('href="#" class="mobile-nav__link mobile-nav__link--top-level">SHOP', 'href="shop.html" class="mobile-nav__link mobile-nav__link--top-level">SHOP'),
    ('href="#" class="site-nav__link site-nav__link--underline site-nav__link--has-dropdown">SHOP', 'href="shop.html" class="site-nav__link site-nav__link--underline site-nav__link--has-dropdown">SHOP'),
    ('href="#" class="site-nav__dropdown-link">', 'href="shop.html" class="site-nav__dropdown-link">'),
    ('href="#" class="mobile-nav__sublist-link">', 'href="shop.html" class="mobile-nav__sublist-link">'),
    ('<p class="login-drawer__footer"><a href="#">Forgot password?</a> · <a href="#">Create account</a></p>',
     '<p class="login-drawer__footer"><a href="login.html">Forgot password?</a> · <a href="signup.html">Create account</a></p>'),
    ('<li class="mobile-nav__item"><span class="mobile-nav__link js-login-open"', '<li class="mobile-nav__item"><a href="login.html" class="mobile-nav__link"'),
]

for a, b in replacements:
    shell = shell.replace(a, b)

# Fix mobile log in closing tag
shell = shell.replace(
    '<li class="mobile-nav__item"><a href="login.html" class="mobile-nav__link" role="button" tabindex="0">Log in</span></li>',
    '<li class="mobile-nav__item"><a href="login.html" class="mobile-nav__link">Log in</a></li>'
)

# Replace header icons block with spaced list version
old_icons = '''          <div class="header-item header-item--icons">
            <a href="#" class="site-nav__link site-nav__link--icon medium-up--hide js-search-open" aria-label="Search">
              <svg class="icon icon-search" viewBox="0 0 64 64" aria-hidden="true"><path d="M47.16 28.58A18.58 18.58 0 1 1 28.58 10a18.58 18.58 0 0 1 18.58 18.58zM54 54L41.94 42"/></svg>
            </a>
            <span class="site-nav__link site-nav__link--icon site-nav__login small--hide js-login-open" role="button" tabindex="0" aria-label="Log in">
              <svg aria-hidden="true" focusable="false" role="presentation" class="icon icon-user" viewBox="0 0 64 64"><path d="M35 39.84v-2.53c3.3-1.91 6-6.66 6-11.41 0-7.63 0-13.82-9-13.82s-9 6.19-9 13.82c0 4.75 2.7 9.51 6 11.41v2.53c-10.18.85-18 6-18 12.16h42c0-6.19-7.82-11.31-18-12.16z"/></svg>
              <span class="visually-hidden">Log in</span>
            </span>
            <button type="button" class="site-nav__link site-nav__link--icon js-cart-open" aria-label="Cart">
              <svg class="icon icon-cart" viewBox="0 0 64 64" aria-hidden="true"><path d="M14 17.44h46.79L53 49H11.21L8.5 8.5H2"/><circle cx="20" cy="54" r="4"/><circle cx="46" cy="54" r="4"/></svg>
            </button>
          </div>'''

new_icons = '''          <div class="header-item header-item--icons">
            <ul class="site-nav__icons" role="list">
              <li class="site-nav__icons-item">
                <button type="button" class="site-nav__link site-nav__link--icon js-search-open medium-up--hide" aria-label="Search">
                  <svg class="icon icon-search" viewBox="0 0 64 64" aria-hidden="true"><path d="M47.16 28.58A18.58 18.58 0 1 1 28.58 10a18.58 18.58 0 0 1 18.58 18.58zM54 54L41.94 42"/></svg>
                </button>
              </li>
              <li class="site-nav__icons-item small--hide">
                <a href="login.html" class="site-nav__link site-nav__link--icon" aria-label="Log in">
                  <svg aria-hidden="true" class="icon icon-user" viewBox="0 0 64 64"><path d="M35 39.84v-2.53c3.3-1.91 6-6.66 6-11.41 0-7.63 0-13.82-9-13.82s-9 6.19-9 13.82c0 4.75 2.7 9.51 6 11.41v2.53c-10.18.85-18 6-18 12.16h42c0-6.19-7.82-11.31-18-12.16z"/></svg>
                  <span class="visually-hidden">Log in</span>
                </a>
              </li>
              <li class="site-nav__icons-item">
                <a href="shop.html" class="site-nav__link site-nav__link--icon small--hide" aria-label="Shop">
                  <svg class="icon icon-shop" viewBox="0 0 64 64" aria-hidden="true"><path d="M8 8h8l6 32h20l6-24H18"/><circle cx="26" cy="54" r="4"/><circle cx="46" cy="54" r="4"/></svg>
                  <span class="visually-hidden">Shop</span>
                </a>
              </li>
              <li class="site-nav__icons-item">
                <button type="button" class="site-nav__link site-nav__link--icon js-cart-open" aria-label="Cart">
                  <svg class="icon icon-cart" viewBox="0 0 64 64" aria-hidden="true"><path d="M14 17.44h46.79L53 49H11.21L8.5 8.5H2"/><circle cx="20" cy="54" r="4"/><circle cx="46" cy="54" r="4"/></svg>
                  <span class="visually-hidden">Cart</span>
                </button>
              </li>
            </ul>
          </div>'''

if old_icons in shell:
    shell = shell.replace(old_icons, new_icons)

open('partials/shell.html', 'w', encoding='utf-8').write(shell)
print('shell.html', len(shell))

# footer
fstart = html.find('<!-- Footer -->')
fend = html.find('<!-- Smart Accessibility widget -->')
open('partials/footer.html', 'w', encoding='utf-8').write(html[fstart:fend])
print('footer.html')

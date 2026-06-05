import os

ROOT = os.path.dirname(os.path.abspath(__file__))
CONTENT = os.path.join(ROOT, 'content')

HEAD = '''<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <meta name="theme-color" content="#1E3AFF">
  <title>{title}</title>
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Lato:ital,wght@0,400;0,600;1,400;1,600&family=Montserrat:wght@400;500;600&display=swap" rel="stylesheet">
  <link rel="stylesheet" href="css/style.css">
  <link rel="stylesheet" href="css/country-flags.css">
  <link rel="stylesheet" href="css/auth.css">
  <link rel="stylesheet" href="css/contact.css">
  <link rel="stylesheet" href="css/policy.css">
  <link rel="stylesheet" href="css/responsive.css">
  <link rel="stylesheet" href="css/pages.css">
  <link rel="stylesheet" href="css/paperform-mobile-sports.css">
  <link rel="stylesheet" href="https://cdn.shopify.com/extensions/019d9b3d-db05-79e1-ad33-4ab8d9a31d79/smart-accessibility-1-24/assets/sa-widget.css">
  <link rel="stylesheet" href="css/a11y-support.css">
  <script>window.sa_shop_domain = 'local';</script>
  <script src="js/a11y-settings.js"></script>
</head>
<body{body_attrs}>
'''

PAPERFORM_SCRIPT = '''  <script src="js/paperform-mobile-sports.js"></script>
  <script>
    (function () {
      var s = document.createElement('script');
      s.src = 'https://paperform.co/__embed.min.js';
      document.body.appendChild(s);
    })();
  </script>'''

TAIL = '''
  <script src="https://cdn.shopify.com/extensions/019d9b3d-db05-79e1-ad33-4ab8d9a31d79/smart-accessibility-1-24/assets/sa-widget.js"></script>
  <script src="js/currencies.js"></script>
  <script src="js/app.js?v=9"></script>
{extra}
</body>
</html>
'''


def load_fragment(stem):
    path = os.path.join(CONTENT, stem + '.fragment.html')
    if os.path.isfile(path):
        return open(path, encoding='utf-8').read()
    return '<div class="rte rte--nomargin"><p>Content is loading. Please check back soon.</p></div>'


def policy_main(title, stem):
    return f'''
  <main class="main-content policy-page" id="MainContent">
    <div class="page-width page-width--narrow page-content">
      <header class="section-header">
        <h1 class="section-header__title">{title}</h1>
      </header>
      {load_fragment(stem)}
    </div>
  </main>
'''


def embed_main(title, paperform_id, dark=False):
    wrap_class = ' paperform-wrapper--dark' if dark else ''
    page_class = ' pro-series-page' if dark else ' page-embed'
    return f'''
  <main class="main-content" id="MainContent">
    <div class="page-width page-width--narrow page-content{page_class}">
      <header class="section-header">
        <h1 class="section-header__title">{title}</h1>
      </header>
      <div class="rte rte--nomargin">
        <div class="paperform-wrapper{wrap_class}">
          <div data-paperform-id="{paperform_id}"></div>
        </div>
      </div>
    </div>
  </main>
'''


# JerseyBird body attributes (Impulse theme – same as live site)
JB_ATTRS = (
    ' data-center-text="true" data-button_style="angled"'
    ' data-type_header_capitalize="true" data-type_headers_align_text="true"'
    ' data-type_product_capitalize="true" data-swatch_style="round"'
)


shell = open(os.path.join(ROOT, 'partials/shell.html'), encoding='utf-8').read()
footer = open(os.path.join(ROOT, 'partials/footer.html'), encoding='utf-8').read()

a11y = open(os.path.join(ROOT, 'partials/a11y-widget.html'), encoding='utf-8').read()
a11y = a11y.replace('shopjerseybird.myshopify.com', 'local')

pages = {
    'index.html': (
        'START A PROJECT',
        '''
  <main class="main-content" id="MainContent">
    <div class="page-width page-width--form page-content">
      <header class="section-header">
        <h1 class="section-header__title">START A PROJECT</h1>
      </header>
      <div class="paperform-wrapper">
        <div data-paperform-id="u2uissty"></div>
      </div>
    </div>
  </main>
''',
        PAPERFORM_SCRIPT
    ),
    'login.html': (
        'Log in',
        '''
  <main class="main-content" id="MainContent">
    <div class="page-width page-width--tiny page-content">
      <header class="section-header">
        <h1 class="section-header__title">Login</h1>
      </header>
      <div class="note note--success hide" id="ResetSuccess">
        We've sent you an email with a link to update your password.
      </div>
      <div id="CustomerLoginForm" class="form-vertical">
        <form id="pageLoginForm" action="index.html" method="post">
          <label for="CustomerEmail">Email</label>
          <input type="email" name="customer[email]" id="CustomerEmail" class="input-full" required autocomplete="email" autocorrect="off" autocapitalize="off">
          <div class="grid">
            <div class="grid__item one-half">
              <label for="CustomerPassword">Password</label>
            </div>
            <div class="grid__item one-half text-right">
              <small class="label-info">
                <a href="#recover" id="RecoverPassword">Forgot password?</a>
              </small>
            </div>
          </div>
          <input type="password" name="customer[password]" id="CustomerPassword" class="input-full" required autocomplete="current-password">
          <p class="login-form__actions">
            <button type="submit" class="btn btn--full">Sign In</button>
          </p>
          <p class="login-form__register"><a href="signup.html" id="customer_register_link">Create account</a></p>
        </form>
      </div>
      <div id="RecoverPasswordForm" class="hide">
        <div class="form-vertical">
          <h2>Reset your password</h2>
          <p>We will send you an email to reset your password.</p>
          <form id="recoverPasswordForm" action="#" method="post">
            <label for="RecoverEmail">Email</label>
            <input type="email" name="email" id="RecoverEmail" class="input-full" required autocorrect="off" autocapitalize="off">
            <p>
              <button type="submit" class="btn">Submit</button>
            </p>
            <button type="button" id="HideRecoverPasswordLink">Cancel</button>
          </form>
        </div>
      </div>
    </div>
  </main>
''',
        '  <script src="js/auth.js"></script>'
    ),
    'signup.html': (
        'Create account',
        '''
  <main class="main-content" id="MainContent">
    <div class="page-width page-width--tiny page-content">
      <header class="section-header">
        <h1 class="section-header__title">Create Account</h1>
      </header>
      <div class="form-vertical">
        <form id="pageSignupForm" action="index.html" method="post">
          <label for="FirstName">First Name</label>
          <input type="text" name="customer[first_name]" id="FirstName" class="input-full" required autocomplete="given-name" autocapitalize="words">
          <label for="LastName">Last Name</label>
          <input type="text" name="customer[last_name]" id="LastName" class="input-full" required autocomplete="family-name" autocapitalize="words">
          <label for="Email">Email</label>
          <input type="email" name="customer[email]" id="Email" class="input-full" required autocomplete="email" autocorrect="off" autocapitalize="off">
          <label for="CreatePassword">Password</label>
          <input type="password" name="customer[password]" id="CreatePassword" class="input-full" required autocomplete="new-password" minlength="8">
          <p>
            <input type="submit" value="Create" class="btn btn--full">
          </p>
        </form>
        <p><a href="login.html">Log in</a></p>
      </div>
    </div>
  </main>
''',
        '  <script src="js/auth.js"></script>'
    ),
    'shop.html': (
        'Shop',
        '''
  <main class="main-content" id="MainContent">
    <div class="page-width page-content">
      <header class="section-header">
        <h1 class="section-header__title">SHOP</h1>
      </header>
      <p class="shop-intro">Browse team collections and apparel. All links stay on this site.</p>
      <ul class="shop-grid">
        <li><a href="collection.html?c=1984-salihlispor" class="shop-card">1984 Salihlispor</a></li>
        <li><a href="collection.html?c=al-qabila-fc" class="shop-card">Al Qabila FC</a></li>
        <li><a href="collection.html?c=bowleys-athletic-club" class="shop-card">Bowley's Athletic Club</a></li>
        <li><a href="collection.html?c=cuenca-jrs" class="shop-card">Cuenca Juniors</a></li>
        <li><a href="product.html?p=fcb-magpies" class="shop-card">FCB Magpies</a></li>
        <li><a href="collection.html?c=jerseybird-night-2025" class="shop-card">JerseyBird Night 2025</a></li>
        <li><a href="collection.html?c=herrera-fc" class="shop-card">Herrera FC</a></li>
        <li><a href="collection.html?c=kahawa-pride-fc" class="shop-card">Kahawa Pride FC</a></li>
        <li><a href="membership.html" class="shop-card">Kahawa Pride FC Discord Membership</a></li>
        <li><a href="collection.html?c=philippines-national-team" class="shop-card">Philippines Men's National Football Team</a></li>
        <li><a href="product.html?p=vv-vianen" class="shop-card">VV Vianen</a></li>
        <li><a href="collection.html?c=walton-hersham-fc" class="shop-card">Walton &amp; Hersham</a></li>
        <li><a href="collection.html?c=jerseybird-apparel" class="shop-card">JerseyBird Apparel</a></li>
      </ul>
    </div>
  </main>
''',
        ''
    ),
    'collection.html': (
        'Collection',
        '''
  <main class="main-content collection-page" id="MainContent">
    <div class="page-width page-content page-content--top">
      <header class="section-header section-header--flush">
        <h1 class="section-header__title" id="collectionTitle">COLLECTION</h1>
      </header>
    </div>
    <div class="collection-content page-width">
      <p class="collection-empty" id="collectionEmpty" hidden>Collection not found.</p>
      <ul class="grid grid--uniform collection-grid" id="collectionProductGrid"></ul>
    </div>
  </main>
''',
        '  <script src="js/collections-data.js"></script>\n  <script src="js/collection-page.js"></script>'
    ),
    'product.html': (
        'Product',
        '''
  <main class="main-content product-page-main" id="MainContent">
    <div class="page-width page-content product-page">
      <p><a href="shop.html" id="productBackLink" class="text-link">← Back to shop</a></p>
      <div class="product-page__layout">
        <div class="product-page__media">
          <span id="productBadge" class="grid-product__tag grid-product__tag--sold-out" hidden>Sold Out</span>
          <div class="product-page__image-wrap">
            <img id="productImage" class="product-page__image" src="" alt="" width="720" height="720" hidden>
          </div>
        </div>
        <div class="product-page__info">
          <header class="section-header section-header--flush">
            <h1 class="section-header__title" id="productTitle">PRODUCT</h1>
          </header>
          <p class="product-page__price" id="productPrice"></p>
          <p class="product-page__description" id="productDescription"></p>
        </div>
      </div>
    </div>
  </main>
''',
        '  <script src="js/collections-data.js"></script>\n  <script src="js/product-page.js"></script>'
    ),
    'reorder.html': (
        'JERSEYBIRD REORDER',
        embed_main('JERSEYBIRD REORDER', 'reorder'),
        PAPERFORM_SCRIPT
    ),
    'on-tour.html': (
        'JerseyBird On Tour',
        embed_main('JerseyBird On Tour', 'l8igwbce'),
        PAPERFORM_SCRIPT
    ),
    'membership.html': (
        "The Lion's Den Kahawa Pride FC Discord Membership",
        '''
  <main class="main-content membership-page" id="MainContent">
    <div class="page-width page-width--narrow page-content">
      <header class="section-header">
        <h1 class="section-header__title">The Lion's Den Kahawa Pride FC Discord Membership</h1>
      </header>
      <div class="rte rte--nomargin">
        <script async src="https://js.stripe.com/v3/pricing-table.js"></script>
        <stripe-pricing-table pricing-table-id="prctbl_1SIGlcAYTw6jY1bocS4DZHCM" publishable-key="pk_live_2W7YQn7Nmo1dLasF3nQ1bWIm00nBdPYBTz"></stripe-pricing-table>
        <div class="membership-terms">
          <strong>Subscription Terms</strong><br><br>
          This is a recurring monthly membership. You will be charged the selected price today and automatically every 30 days until you cancel.<br><br>
          You may cancel at any time through your Stripe Customer Portal
          <a href="https://billing.stripe.com/p/login/7sY14mdq64v7enS7LqefC00" target="_blank" rel="noopener">here</a>.<br><br>
          By subscribing, you agree to our <a href="terms.html">Terms &amp; Conditions</a>.
        </div>
      </div>
    </div>
  </main>
''',
        ''
    ),
    'about.html': (
        'What is JerseyBird?',
        '''
  <main class="main-content about-page" id="MainContent">
    <div class="page-width page-content">
      <header class="section-header">
        <h1 class="section-header__title">WHAT IS JERSEYBIRD?</h1>
      </header>
      <div class="rte about-rte text-center">
        <p>JerseyBird is a sportswear design and manufacturing company.</p>
        <p>From national teams to youth clubs, we work 1-on-1 with teams to create custom jerseys and apparel for all sports.</p>
        <p>Our mission: become the world's premier sportswear manufacturer through world class products, world class athletics, and captivating stories.</p>
        <h2>WHO DO WE WORK WITH?</h2>
        <p>Since 2019, we've been working with teams from around the world to create bespoke apparel.</p>
        <p>These are a few of our best projects.</p>
        <p><a href="index.html" class="text-link">Start a Project</a> · <a href="contact.html" class="text-link">Contact us</a></p>
      </div>
    </div>
  </main>
''',
        ''
    ),
    'contact.html': (
        'Contact us',
        '''
  <main class="main-content contact-page-main" id="MainContent">
    <div class="page-width page-width--narrow page-content">
      <div class="contact-intro text-center">
        <h2 class="contact-intro__title">Get in touch</h2>
        <div class="contact-intro__rte">
          <p>If you have any questions or comments for us, fill out the form below with all of your details and we'll get back to you as soon as possible.</p>
          <p>Our support team is active from 9AM - 5PM (EST) Monday - Friday.</p>
        </div>
      </div>
      <header class="section-header section-header--contact">
        <h2 class="section-header__title">Contact us</h2>
      </header>
      <div class="form-vertical contact-form-block">
        <form class="contact-form" id="contactForm" action="#" method="post">
          <div class="grid grid--small">
            <div class="grid__item medium-up--one-half">
              <label for="ContactFormName">Name</label>
              <input type="text" id="ContactFormName" class="input-full" name="contact[name]" required autocapitalize="words">
            </div>
            <div class="grid__item medium-up--one-half">
              <label for="ContactFormEmail">Email</label>
              <input type="email" id="ContactFormEmail" class="input-full" name="contact[email]" required autocorrect="off" autocapitalize="off">
            </div>
          </div>
          <label for="ContactFormMessage">Message</label>
          <textarea rows="5" id="ContactFormMessage" class="input-full" name="contact[body]" required></textarea>
          <p class="contact-form__submit">
            <button type="submit" class="btn btn--full">Send</button>
          </p>
          <p class="contact-form__disclaimer">This site is protected by hCaptcha and the hCaptcha <a href="https://hcaptcha.com/privacy" target="_blank" rel="noopener">Privacy Policy</a> and <a href="https://hcaptcha.com/terms" target="_blank" rel="noopener">Terms of Service</a> apply.</p>
        </form>
      </div>
    </div>
  </main>
''',
        '  <script src="js/auth.js"></script>'
    ),
    'search.html': (
        'Search',
        '''
  <main class="main-content search-page" id="MainContent">
    <div class="search-content" data-section-type="collection-grid">
      <div class="page-width page-content">
        <header class="section-header">
          <h1 class="section-header__title">Search</h1>
        </header>
        <form action="search.html" method="get" class="input-group search-bar search-bar--page" role="search" id="pageSearchForm">
          <input type="hidden" name="type" value="product,article,page,collection">
          <input type="hidden" name="options[prefix]" value="last">
          <input type="search" name="q" id="SearchInput" class="input-group-field" placeholder="Search our store" aria-label="Search our store" autocomplete="off">
          <div class="input-group-btn">
            <button type="submit" class="btn">
              <svg class="icon icon-search" viewBox="0 0 64 64" aria-hidden="true"><path d="M47.16 28.58A18.58 18.58 0 1 1 28.58 10a18.58 18.58 0 0 1 18.58 18.58zM54 54L41.94 42"/></svg>
              <span class="visually-hidden">Search</span>
            </button>
          </div>
        </form>
        <div id="searchResultsArea" class="search-results-area" hidden>
          <p class="search-results__count" id="searchResultsCount"></p>
          <p class="search-results__empty" id="searchEmpty" hidden>No results could be found. Try checking your spelling or using different words.</p>
          <ul class="product-grid" id="searchProductGrid"></ul>
        </div>
      </div>
    </div>
  </main>
''',
        '  <script src="js/products-data.js"></script>\n  <script src="js/search.js"></script>'
    ),
    'faqs.html': ('FAQs', policy_main('FAQs', 'faqs'), ''),
    'shipping-policy.html': ('Shipping Policy', policy_main('Shipping Policy', 'shipping-policy'), ''),
    'returns-policy.html': ('Returns & Refunds Policy', policy_main('Returns & Refunds Policy', 'returns-policy'), ''),
    'terms.html': ('Terms and Conditions', policy_main('Terms and Conditions', 'terms'), ''),
    'privacy.html': ('Privacy policy', policy_main('Privacy policy', 'privacy'), ''),
    'ambassador.html': (
        'JerseyBird Ambassador Application',
        embed_main('JerseyBird Ambassador Application', '2b2yuzzd'),
        PAPERFORM_SCRIPT
    ),
    'pro-series.html': (
        'JerseyBird Pro Series',
        embed_main('JerseyBird Pro Series', 'c7alm0ye', dark=True),
        PAPERFORM_SCRIPT
    ),
}

BODY_ATTRS = {
    'index.html': ' class="template-page template-page-home"' + JB_ATTRS,
    'shop.html': ' class="template-page"' + JB_ATTRS,
    'collection.html': ' class="template-collection"' + JB_ATTRS,
    'product.html': ' class="template-product"' + JB_ATTRS,
    'reorder.html': ' class="template-page"' + JB_ATTRS,
    'on-tour.html': ' class="template-page"' + JB_ATTRS,
    'membership.html': ' class="template-page"' + JB_ATTRS,
    'about.html': ' class="template-page"' + JB_ATTRS,
    'login.html': ' class="template-customers-login" data-center-text="true" data-button_style="angled"',
    'signup.html': ' class="template-customers-register" data-center-text="true" data-button_style="angled"',
    'contact.html': ' class="template-page template-page-contact"' + JB_ATTRS,
    'search.html': ' class="template-search" data-center-text="true" data-type_headers_align_text="true" data-button_style="angled"',
    'faqs.html': ' class="template-page template-page-policy"' + JB_ATTRS,
    'shipping-policy.html': ' class="template-page template-page-policy"' + JB_ATTRS,
    'returns-policy.html': ' class="template-page template-page-policy"' + JB_ATTRS,
    'terms.html': ' class="template-page template-page-policy"' + JB_ATTRS,
    'privacy.html': ' class="template-page template-page-policy"' + JB_ATTRS,
    'ambassador.html': ' class="template-page template-page-policy"' + JB_ATTRS,
    'pro-series.html': ' class="template-page template-page-pro-series" data-center-text="true" data-button_style="angled" data-type_headers_align_text="true"',
}

for fname, (title, main, extra) in pages.items():
    html = HEAD.format(title=title, body_attrs=BODY_ATTRS.get(fname, '')) + shell + main + footer + '\n  <!-- Accessibility -->\n' + a11y + TAIL.format(extra=extra)
    open(fname, 'w', encoding='utf-8').write(html)
    print('wrote', fname)

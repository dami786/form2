(function () {
  'use strict';

  const STORAGE_CURRENCY = 'jb_currency';

  /* ── Utilities ── */
  function qs(sel, ctx) { return (ctx || document).querySelector(sel); }
  function qsa(sel, ctx) { return Array.from((ctx || document).querySelectorAll(sel)); }

  function defaultCurrency() {
    return CURRENCIES.find(function (c) { return c.code === 'AE'; }) || CURRENCIES[0];
  }

  function getStoredCurrency() {
    try {
      const raw = localStorage.getItem(STORAGE_CURRENCY);
      if (!raw) return defaultCurrency();
      const saved = JSON.parse(raw);
      return CURRENCIES.find(function (c) { return c.code === saved.code; }) || defaultCurrency();
    } catch (e) {
      return defaultCurrency();
    }
  }

  function showCurrencyApplying() {
    let el = document.getElementById('currencyApplying');
    if (!el) {
      el = document.createElement('div');
      el.id = 'currencyApplying';
      el.className = 'currency-applying';
      el.innerHTML = '<div class="currency-applying__inner">Updating currency…</div>';
      document.body.appendChild(el);
    }
    el.classList.add('is-visible');
    window.setTimeout(function () {
      el.classList.remove('is-visible');
    }, 600);
  }

  function setStoredCurrency(item) {
    localStorage.setItem(STORAGE_CURRENCY, JSON.stringify(item));
    qsa('[data-currency-flag]').forEach(function (el) {
      el.className = 'currency-flag currency-flag--' + item.flag;
    });
    qsa('[data-currency-label]').forEach(function (el) {
      el.textContent = item.label;
    });
    qsa('.disclosure-list__option').forEach(function (el) {
      const selected = el.getAttribute('data-value') === item.code;
      el.classList.toggle('is-current', selected);
      if (selected) el.setAttribute('aria-current', 'true');
      else el.removeAttribute('aria-current');
    });
  }

  /* ── Body scroll lock ── */
  var scrollY = 0;

  function lockBody(lock) {
    if (lock) {
      scrollY = window.scrollY || window.pageYOffset;
      document.body.classList.add('drawer-open');
      document.body.style.top = '-' + scrollY + 'px';
    } else {
      document.body.classList.remove('drawer-open');
      document.body.style.top = '';
      window.scrollTo(0, scrollY);
    }
  }

  /* ── Drawers (Nav + Cart) ── */
  function openDrawer(id) {
    const drawer = document.getElementById(id);
    const overlay = qs('.drawer-overlay');
    if (!drawer) return;
    qsa('.drawer.is-open').forEach(function (d) {
      d.classList.remove('is-open');
      d.setAttribute('aria-hidden', 'true');
    });
    drawer.classList.add('is-open');
    drawer.setAttribute('aria-hidden', 'false');
    if (overlay) overlay.classList.add('is-visible');
    lockBody(true);
    closeAllDisclosures();
    toggleSearch(false);
    if (id === 'CartDrawer') {
      qsa('.js-cart-open').forEach(function (el) { el.setAttribute('aria-expanded', 'true'); });
    }
    if (id === 'LoginDrawer') {
      drawer.querySelector('input')?.focus();
    }
  }

  function closeDrawers() {
    qsa('.drawer').forEach(function (d) {
      d.classList.remove('is-open');
      d.setAttribute('aria-hidden', 'true');
    });
    const overlay = qs('.drawer-overlay');
    if (overlay) overlay.classList.remove('is-visible');
    lockBody(false);
    qsa('.js-cart-open').forEach(function (el) {
      el.setAttribute('aria-expanded', 'false');
    });
  }

  qsa('.js-drawer-open-nav').forEach(function (btn) {
    btn.addEventListener('click', function () { openDrawer('NavDrawer'); });
  });
  qsa('.js-cart-open').forEach(function (btn) {
    btn.addEventListener('click', function (e) {
      e.preventDefault();
      openDrawer('CartDrawer');
    });
  });
  /* Profile icon opens login.html (full account page), not a drawer */
  qsa('.js-drawer-close, .js-cart-close, .js-login-close').forEach(function (el) {
    el.addEventListener('click', closeDrawers);
  });
  qs('.drawer-overlay')?.addEventListener('click', closeDrawers);

  document.getElementById('loginForm')?.addEventListener('submit', function (e) {
    e.preventDefault();
    closeDrawers();
  });

  document.getElementById('headerSearchForm')?.addEventListener('submit', function (e) {
    e.preventDefault();
    const q = e.target.querySelector('input[name="q"]')?.value?.trim();
    if (q) alert('Search: ' + q);
    toggleSearch(false);
  });

  /* ── Search overlay ── */
  const searchContainer = document.getElementById('SearchContainer');
  let searchOpen = false;

  function toggleSearch(open) {
    if (!searchContainer) return;
    searchOpen = open;
    searchContainer.hidden = !open;
    if (open) {
      searchContainer.querySelector('input')?.focus();
      closeDrawers();
      closeAllDisclosures();
    }
  }

  qsa('.js-search-open').forEach(function (btn) {
    btn.addEventListener('click', function (e) {
      e.preventDefault();
      toggleSearch(!searchOpen);
    });
  });
  qsa('.js-search-close').forEach(function (btn) {
    btn.addEventListener('click', function () { toggleSearch(false); });
  });

  /* ── Mobile nav accordion ── */
  qsa('.mobile-nav .collapsible-trigger').forEach(function (btn) {
    btn.addEventListener('click', function () {
      const item = btn.closest('.mobile-nav__item');
      const sublist = item?.querySelector('.mobile-nav__sublist');
      if (!sublist) return;
      const open = btn.getAttribute('aria-expanded') === 'true';
      btn.setAttribute('aria-expanded', String(!open));
      sublist.hidden = open;
    });
  });

  /* ── Desktop nav dropdown (click for touch) ── */
  qsa('.site-nav--has-dropdown > .site-nav__link--has-dropdown').forEach(function (link) {
    link.addEventListener('click', function (e) {
      if (window.innerWidth < 769) return;
      const parent = link.closest('.site-nav--has-dropdown');
      const isOpen = parent.classList.contains('is-open');
      qsa('.site-nav--has-dropdown.is-open').forEach(function (el) {
        el.classList.remove('is-open');
      });
      if (!isOpen) {
        e.preventDefault();
        parent.classList.add('is-open');
      }
    });
  });
  document.addEventListener('click', function (e) {
    if (!e.target.closest('.site-nav--has-dropdown')) {
      qsa('.site-nav--has-dropdown.is-open').forEach(function (el) {
        el.classList.remove('is-open');
      });
    }
  });

  /* ── Currency disclosure (matches JerseyBird Shopify localization UI) ── */
  function buildCurrencyLists() {
    const lists = ['CurrencyList-toolbar', 'CurrencyList-footer'];
    const current = getStoredCurrency();

    lists.forEach(function (listId) {
      const ul = document.getElementById(listId);
      if (!ul) return;
      ul.innerHTML = '';
      CURRENCIES.forEach(function (c) {
        const li = document.createElement('li');
        li.className = 'disclosure-list__item';
        const link = document.createElement('a');
        link.href = '#';
        link.className = 'disclosure-list__option' + (c.code === current.code ? ' is-current' : '');
        link.setAttribute('data-value', c.code);
        link.setAttribute('data-disclosure-option', '');
        if (c.code === current.code) link.setAttribute('aria-current', 'true');
        const flag = document.createElement('span');
        flag.className = 'currency-flag currency-flag--' + c.flag;
        flag.setAttribute('aria-hidden', 'true');
        const label = document.createElement('span');
        label.className = 'disclosure-list__label';
        label.textContent = c.label;
        link.appendChild(flag);
        link.appendChild(label);
        link.addEventListener('click', function (e) {
          e.preventDefault();
          setStoredCurrency(c);
          closeAllDisclosures();
          showCurrencyApplying();
        });
        li.appendChild(link);
        ul.appendChild(li);
      });
    });
    setStoredCurrency(current);
  }

  function closeAllDisclosures() {
    qsa('[data-disclosure-currency].is-open, .disclosure--currency.is-open').forEach(function (d) {
      d.classList.remove('is-open');
      const toggle = d.querySelector('.disclosure__toggle');
      const list = d.querySelector('.disclosure-list');
      if (toggle) toggle.setAttribute('aria-expanded', 'false');
      if (list) list.hidden = true;
    });
  }

  function openCurrencyDisclosure(disclosure) {
    const btn = disclosure.querySelector('.js-currency-toggle');
    const list = disclosure.querySelector('.disclosure-list');
    disclosure.classList.add('is-open');
    if (btn) btn.setAttribute('aria-expanded', 'true');
    if (list) {
      list.hidden = false;
      const current = list.querySelector('.disclosure-list__option.is-current');
      if (current) current.scrollIntoView({ block: 'nearest' });
    }
  }

  qsa('.js-currency-toggle').forEach(function (btn) {
    btn.addEventListener('click', function (e) {
      e.preventDefault();
      e.stopPropagation();
      const disclosure = btn.closest('[data-disclosure-currency], .disclosure--currency');
      const open = disclosure.classList.contains('is-open');
      closeAllDisclosures();
      if (!open) openCurrencyDisclosure(disclosure);
    });
  });
  document.addEventListener('click', function (e) {
    if (!e.target.closest('.disclosure--currency')) closeAllDisclosures();
  });

  /* ── Footer newsletter ── */
  document.getElementById('footerNewsletter')?.addEventListener('submit', function (e) {
    e.preventDefault();
    const email = e.target.querySelector('input[type="email"]')?.value;
    if (!email) return;
    alert('Thanks for subscribing! You will receive your free design draft offer at ' + email);
    e.target.reset();
  });

  qsa('.js-footer-toggle').forEach(function (btn) {
    btn.addEventListener('click', function () {
      const open = btn.getAttribute('aria-expanded') === 'true';
      btn.setAttribute('aria-expanded', String(!open));
      const panel = document.getElementById(btn.getAttribute('aria-controls'));
      if (panel) panel.hidden = open;
    });
  });

  /* ── Global keyboard ── */
  document.addEventListener('keydown', function (e) {
    if (e.key === 'Escape') {
      closeDrawers();
      toggleSearch(false);
      closeAllDisclosures();
    }
  });

  /* ── Skip link ── */
  qs('.skip-link')?.addEventListener('click', function () {
    closeDrawers();
    toggleSearch(false);
  });

  /* ── Init ── */
  buildCurrencyLists();
})();

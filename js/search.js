(function () {
  'use strict';

  var products = window.SITE_PRODUCTS || [];
  var form = document.getElementById('pageSearchForm');
  var input = document.getElementById('SearchInput');
  var area = document.getElementById('searchResultsArea');
  var grid = document.getElementById('searchProductGrid');
  var empty = document.getElementById('searchEmpty');
  var countEl = document.getElementById('searchResultsCount');

  function getQuery() {
    return new URLSearchParams(window.location.search).get('q') || '';
  }

  function matchProduct(p, q) {
    var lower = q.toLowerCase();
    return p.title.toLowerCase().indexOf(lower) !== -1 ||
      (p.tags && p.tags.indexOf(lower) !== -1) ||
      (p.handle && p.handle.indexOf(lower.replace(/\s+/g, '-')) !== -1);
  }

  function productUrl(p) {
    if (p.url) return p.url;
    if (p.collection) return 'collection.html?c=' + encodeURIComponent(p.collection);
    return 'shop.html';
  }

  function renderGrid(hits, q) {
    if (!area || !grid) return;

    if (!q) {
      area.hidden = true;
      return;
    }

    area.hidden = false;
    if (countEl) {
      countEl.textContent = hits.length
        ? hits.length + ' result' + (hits.length === 1 ? '' : 's') + ' for “' + q + '”'
        : '';
    }

    grid.innerHTML = '';
    if (!hits.length) {
      if (empty) empty.hidden = false;
      return;
    }

    if (empty) empty.hidden = true;
    hits.forEach(function (p) {
      var li = document.createElement('li');
      li.className = 'product-card';
      var a = document.createElement('a');
      a.href = productUrl(p);
      a.innerHTML =
        '<span class="product-card__image" aria-hidden="true"></span>' +
        '<span class="product-card__title">' + p.title + '</span>';
      li.appendChild(a);
      grid.appendChild(li);
    });
  }

  function runSearch(q) {
    q = (q || '').trim();
    if (input) input.value = q;
    if (!q) {
      renderGrid([], '');
      return;
    }
    var hits = products.filter(function (p) {
      return matchProduct(p, q);
    });
    renderGrid(hits, q);
  }

  if (form) {
    form.addEventListener('submit', function (e) {
      var q = input && input.value ? input.value.trim() : '';
      if (!q) {
        e.preventDefault();
        return;
      }
      e.preventDefault();
      window.location.href = 'search.html?q=' + encodeURIComponent(q);
    });
  }

  runSearch(getQuery());
})();

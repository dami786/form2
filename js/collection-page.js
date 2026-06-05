(function () {
  'use strict';

  var collections = window.SITE_COLLECTIONS || {};
  var handle = new URLSearchParams(window.location.search).get('c');
  var col = handle && collections[handle];
  var titleEl = document.getElementById('collectionTitle');
  var grid = document.getElementById('collectionProductGrid');
  var empty = document.getElementById('collectionEmpty');

  if (!col) {
    if (titleEl) titleEl.textContent = 'COLLECTION';
    if (empty) empty.hidden = false;
    document.title = 'Collection — JerseyBird';
    return;
  }

  if (titleEl) titleEl.textContent = col.title;
  document.title = col.title + ' — JerseyBird';

  if (!grid) return;

  if (!col.products.length) {
    if (empty) {
      empty.textContent = 'No products in this collection yet.';
      empty.hidden = false;
    }
    return;
  }

  col.products.forEach(function (p) {
    var li = document.createElement('li');
    li.className = 'grid__item grid-product small--one-half medium-up--one-quarter';
    var tag = p.soldOut
      ? '<span class="grid-product__tag grid-product__tag--sold-out">Sold Out</span>'
      : '';
    var imgHtml = p.image
      ? '<img class="grid-product__img" src="' + p.image + '" alt="" loading="lazy" width="540" height="540">'
      : '<span class="grid-product__placeholder" aria-hidden="true"></span>';
    li.innerHTML =
      '<div class="grid-product__content">' +
      tag +
      '<a href="product.html?p=' + encodeURIComponent(p.handle) + '&c=' + encodeURIComponent(handle) + '" class="grid-product__link">' +
      '<div class="grid-product__image-mask"><div class="grid__image-ratio grid__image-ratio--square">' + imgHtml + '</div></div>' +
      '<div class="grid-product__meta">' +
      '<div class="grid-product__title grid-product__title--heading">' + p.title + '</div>' +
      '<div class="grid-product__price">' + p.price + '</div>' +
      '</div></a></div>';
    grid.appendChild(li);
  });
})();

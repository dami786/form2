(function () {
  'use strict';

  var params = new URLSearchParams(window.location.search);
  var handle = params.get('p');
  var collectionHandle = params.get('c');
  var products = window.SITE_PRODUCT_PAGES || {};
  var collections = window.SITE_COLLECTIONS || {};
  var product = handle && products[handle];
  var titleEl = document.getElementById('productTitle');
  var priceEl = document.getElementById('productPrice');
  var descEl = document.getElementById('productDescription');
  var badgeEl = document.getElementById('productBadge');
  var backEl = document.getElementById('productBackLink');
  var imgEl = document.getElementById('productImage');

  function findInCollection() {
    if (!collectionHandle || !collections[collectionHandle]) return null;
    var list = collections[collectionHandle].products || [];
    for (var i = 0; i < list.length; i++) {
      if (list[i].handle === handle) return list[i];
    }
    return null;
  }

  var fromCol = findInCollection();
  var data = product || fromCol;

  if (!data) {
    if (titleEl) titleEl.textContent = 'PRODUCT';
    document.title = 'Product — JerseyBird';
    return;
  }

  var title = data.title;
  if (titleEl) titleEl.textContent = title;
  document.title = title + ' — JerseyBird';
  if (priceEl) priceEl.textContent = data.price || '';
  if (descEl && data.description) descEl.textContent = data.description;
  if (imgEl && data.image) {
    imgEl.src = data.image;
    imgEl.alt = title;
    imgEl.hidden = false;
  }
  if (badgeEl && data.soldOut) {
    badgeEl.textContent = 'Sold Out';
    badgeEl.hidden = false;
  }
  if (backEl && collectionHandle && collections[collectionHandle]) {
    backEl.href = 'collection.html?c=' + encodeURIComponent(collectionHandle);
    backEl.textContent = '← Back to ' + collections[collectionHandle].title;
  }
})();

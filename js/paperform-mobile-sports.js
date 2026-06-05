(function () {
  'use strict';

  // Paperform picks optionsColumns vs optionsColumnsMobile from innerWidth on load (< 600px = mobile).
  var MOBILE_MQ = window.matchMedia('(max-width: 600px)');
  var wasMobile = MOBILE_MQ.matches;
  var reloadTimer = null;
  var reloading = false;

  function getPaperformIframe() {
    var wrapper = document.querySelector('.paperform-wrapper');
    return wrapper ? wrapper.querySelector('iframe') : null;
  }

  function reloadPaperformLayout() {
    if (reloading) return;

    var iframe = getPaperformIframe();
    if (!iframe || !iframe.src) return;

    reloading = true;

    try {
      var url = new URL(iframe.src, window.location.href);
      url.searchParams.set('_layout', MOBILE_MQ.matches ? 'mobile' : 'desktop');
      url.searchParams.set('_t', String(Date.now()));
      iframe.src = url.toString();
    } catch (err) {
      iframe.src = iframe.src;
    }

    iframe.addEventListener(
      'load',
      function () {
        reloading = false;
      },
      { once: true }
    );

    setTimeout(function () {
      reloading = false;
    }, 8000);
  }

  function onBreakpointChange(e) {
    var isMobile = e.matches;
    if (isMobile === wasMobile) return;
    wasMobile = isMobile;
    clearTimeout(reloadTimer);
    reloadTimer = setTimeout(reloadPaperformLayout, 150);
  }

  if (typeof MOBILE_MQ.addEventListener === 'function') {
    MOBILE_MQ.addEventListener('change', onBreakpointChange);
  } else if (typeof MOBILE_MQ.addListener === 'function') {
    MOBILE_MQ.addListener(onBreakpointChange);
  }
})();

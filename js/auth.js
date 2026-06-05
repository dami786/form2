(function () {
  'use strict';

  var loginForm = document.getElementById('pageLoginForm');
  var signupForm = document.getElementById('pageSignupForm');
  var recoverForm = document.getElementById('recoverPasswordForm');
  var loginBlock = document.getElementById('CustomerLoginForm');
  var recoverBlock = document.getElementById('RecoverPasswordForm');
  var recoverLink = document.getElementById('RecoverPassword');
  var hideRecover = document.getElementById('HideRecoverPasswordLink');
  var resetSuccess = document.getElementById('ResetSuccess');

  if (recoverLink && loginBlock && recoverBlock) {
    recoverLink.addEventListener('click', function (e) {
      e.preventDefault();
      loginBlock.classList.add('hide');
      recoverBlock.classList.remove('hide');
    });
  }

  if (hideRecover && loginBlock && recoverBlock) {
    hideRecover.addEventListener('click', function () {
      recoverBlock.classList.add('hide');
      loginBlock.classList.remove('hide');
    });
  }

  if (recoverForm) {
    recoverForm.addEventListener('submit', function (e) {
      e.preventDefault();
      recoverBlock.classList.add('hide');
      loginBlock.classList.remove('hide');
      if (resetSuccess) resetSuccess.classList.remove('hide');
    });
  }

  if (loginForm) {
    loginForm.addEventListener('submit', function (e) {
      e.preventDefault();
      window.location.href = 'index.html';
    });
  }

  if (signupForm) {
    signupForm.addEventListener('submit', function (e) {
      e.preventDefault();
      window.location.href = 'index.html';
    });
  }

  document.getElementById('contactForm')?.addEventListener('submit', function (e) {
    e.preventDefault();
    alert('Thanks! We\'ll get back to you as soon as possible.');
    e.target.reset();
  });
})();

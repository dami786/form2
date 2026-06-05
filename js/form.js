(function () {
  'use strict';

  var form = document.getElementById('projectForm');
  if (!form || typeof SPORTS === 'undefined') return;

  var steps = Array.from(form.querySelectorAll('.form-step'));
  var btnBack = form.querySelector('.form-step-actions__btn--back');
  var btnNext = form.querySelector('.form-step-actions__btn--next');
  var actions = form.querySelector('.form-step-actions');
  var sportGrid = form.querySelector('.sport-grid');
  var sportPreview = document.getElementById('sportPreview');
  var sportPreviewIcon = document.getElementById('sportPreviewIcon');
  var sportOtherCard = document.getElementById('sportOtherCard');
  var current = 0;
  var data = { sport: '', sportLabel: '', team: '', name: '', email: '', phone: '', qty: '', notes: '' };

  function qsa(sel, ctx) {
    return Array.from((ctx || document).querySelectorAll(sel));
  }

  function clearSelection() {
    qsa('.sport-card.is-selected', form).forEach(function (c) {
      c.classList.remove('is-selected');
    });
  }

  function updateSportPreview(sportId) {
    if (!sportPreview || !sportPreviewIcon) return;
    if (!sportId || sportId === 'other' || !SPORT_ICONS[sportId]) {
      sportPreview.hidden = true;
      sportPreviewIcon.innerHTML = '';
      return;
    }
    sportPreview.hidden = false;
    sportPreviewIcon.innerHTML = SPORT_ICONS[sportId];
  }

  function selectSport(sport, cardEl) {
    clearSelection();
    if (cardEl) cardEl.classList.add('is-selected');
    data.sport = sport.id;
    data.sportLabel = sport.label;
    updateSportPreview(sport.id);
  }

  function renderSports() {
    if (!sportGrid) return;
    sportGrid.innerHTML = '';
    SPORTS.filter(function (s) { return !s.isOther; }).forEach(function (sport) {
      var card = document.createElement('button');
      card.type = 'button';
      card.className = 'sport-card';
      card.dataset.sport = sport.id;
      var icon = typeof SPORT_ICONS !== 'undefined' ? SPORT_ICONS[sport.id] : '';
      card.innerHTML =
        '<span class="sport-card__radio" aria-hidden="true"></span>' +
        '<span class="sport-card__label">' + sport.label + '</span>' +
        (icon ? '<span class="sport-card__icon">' + icon + '</span>' : '');
      card.addEventListener('click', function () {
        selectSport(sport, card);
      });
      sportGrid.appendChild(card);
    });
  }

  if (sportOtherCard) {
    sportOtherCard.addEventListener('click', function () {
      var other = SPORTS.find(function (s) { return s.isOther; });
      if (!other) return;
      selectSport(other, sportOtherCard);
    });
  }

  function showStep(i) {
    current = i;
    steps.forEach(function (step, idx) {
      step.classList.toggle('is-active', idx === i);
    });
    if (btnBack) {
      btnBack.hidden = i === 0;
      btnBack.disabled = i === 0;
    }
    if (btnNext) {
      btnNext.textContent = i === steps.length - 2 ? 'Submit' : 'Continue';
      btnNext.hidden = i >= steps.length - 1;
    }
    if (actions) {
      actions.hidden = i >= steps.length - 1;
    }
  }

  function validateStep() {
    if (current === 0) {
      if (!data.sport) {
        alert('Please select a sport.');
        return false;
      }
      return true;
    }
    if (current === 1) {
      var team = form.querySelector('#teamName');
      data.team = team?.value.trim() || '';
      if (!data.team) {
        team?.focus();
        alert('Please enter your team or organization name.');
        return false;
      }
      return true;
    }
    if (current === 2) {
      data.name = form.querySelector('#contactName')?.value.trim() || '';
      data.email = form.querySelector('#contactEmail')?.value.trim() || '';
      data.phone = form.querySelector('#contactPhone')?.value.trim() || '';
      if (!data.name || !data.email) {
        alert('Please enter your name and email.');
        return false;
      }
      if (!/^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(data.email)) {
        alert('Please enter a valid email address.');
        return false;
      }
      return true;
    }
    if (current === 3) {
      var qty = form.querySelector('input[name="qty"]:checked');
      data.qty = qty ? qty.value : '';
      data.notes = form.querySelector('#projectNotes')?.value.trim() || '';
      if (!data.qty) {
        alert('Please select an estimated quantity.');
        return false;
      }
      var summary = form.querySelector('#formSummary');
      if (summary) {
        summary.innerHTML =
          '<p><strong>Sport:</strong> ' + data.sportLabel + '</p>' +
          '<p><strong>Team:</strong> ' + data.team + '</p>' +
          '<p><strong>Contact:</strong> ' + data.name + ' · ' + data.email + '</p>' +
          '<p><strong>Quantity:</strong> ' + data.qty + '</p>';
        summary.hidden = false;
      }
      return true;
    }
    return true;
  }

  btnBack?.addEventListener('click', function () {
    if (current > 0) showStep(current - 1);
  });

  btnNext?.addEventListener('click', function () {
    if (!validateStep()) return;
    if (current === 3) {
      showStep(4);
      return;
    }
    if (current < steps.length - 1) showStep(current + 1);
  });

  renderSports();
  showStep(0);
})();

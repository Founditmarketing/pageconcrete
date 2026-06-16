(function () {
  function init() {
    var form = document.querySelector('form[action="#"]');
    if (!form) return;

    var status = document.createElement('p');
    status.id = 'pcf-status';
    status.style.cssText = 'margin-top:14px;font-size:14px;font-weight:600;display:none';
    form.appendChild(status);

    function showStatus(msg, color) {
      status.textContent = msg;
      status.style.color = color;
      status.style.display = 'block';
    }

    form.addEventListener('submit', function (e) {
      e.preventDefault();

      var data = {};
      new FormData(form).forEach(function (val, key) { data[key] = val; });

      var btn = form.querySelector('[type="submit"]');
      var originalText = btn.textContent;
      btn.disabled = true;
      btn.textContent = 'Sending…';
      status.style.display = 'none';

      fetch('/api/send-email', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(data),
      })
        .then(function (r) {
          return r.json().catch(function () {
            throw new Error('Server error (' + r.status + '). Please call us at (336) 962-7934.');
          });
        })
        .then(function (json) {
          if (json.ok) {
            form.reset();
            showStatus('Thank you! We\'ll be in touch shortly.', '#2e7d32');
          } else {
            showStatus(json.error || 'Something went wrong. Please try again.', '#c62828');
          }
          btn.disabled = false;
          btn.textContent = originalText;
        })
        .catch(function (err) {
          showStatus(err && err.message ? err.message : 'Network error. Please call us at (336) 962-7934.', '#c62828');
          btn.disabled = false;
          btn.textContent = originalText;
        });
    });
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', init);
  } else {
    init();
  }
})();

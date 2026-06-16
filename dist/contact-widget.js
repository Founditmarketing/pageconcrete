(function () {
  if (document.getElementById('pcw-root')) return;

  var style = document.createElement('style');
  style.textContent = [
    '#pcw-root{position:fixed;bottom:20px;right:20px;z-index:2147483647;font-family:"Open Sans",Arial,sans-serif;display:flex;flex-direction:column;align-items:flex-end;gap:10px}',
    '#pcw-card{background:#1a8fd1;border-radius:14px;padding:22px 20px 20px;width:250px;box-shadow:0 6px 28px rgba(0,0,0,.28);display:none;flex-direction:column;align-items:center;text-align:center;position:relative;animation:pcw-in .22s ease}',
    '#pcw-card.pcw-open{display:flex}',
    '@keyframes pcw-in{from{opacity:0;transform:translateY(12px)}to{opacity:1;transform:translateY(0)}}',
    '#pcw-avatar{width:72px;height:72px;border-radius:50%;border:3px solid #fff;margin-bottom:13px;background:#0e6fa8;display:flex;align-items:center;justify-content:center;color:#fff}',
    '#pcw-name{color:#fff;font-size:16px;font-weight:700;margin-bottom:3px;line-height:1.3}',
    '#pcw-brand{color:rgba(255,255,255,.75);font-size:10px;font-weight:700;letter-spacing:1.5px;text-transform:uppercase;margin-bottom:12px}',
    '#pcw-body{color:#fff;font-size:13px;line-height:1.55;margin-bottom:17px}',
    '#pcw-phone{color:#ffd84d;font-size:15px;font-weight:700;text-decoration:none;display:flex;align-items:center;gap:6px;background:rgba(0,0,0,.15);padding:8px 14px;border-radius:30px}',
    '#pcw-phone:hover{color:#fff}',
    '#pcw-x{position:absolute;top:8px;right:10px;background:none;border:none;color:rgba(255,255,255,.65);font-size:17px;cursor:pointer;line-height:1;padding:2px 5px}',
    '#pcw-x:hover{color:#fff}',
    '#pcw-trigger{background:#d9302a;color:#fff;border:none;border-radius:30px;padding:13px 20px;font-size:14px;font-weight:700;cursor:pointer;display:flex;align-items:center;gap:8px;box-shadow:0 4px 14px rgba(0,0,0,.3);white-space:nowrap;transition:background .2s}',
    '#pcw-trigger:hover{background:#b52320}',
    '#pcw-trigger svg{flex-shrink:0}'
  ].join('');
  document.head.appendChild(style);

  var root = document.createElement('div');
  root.id = 'pcw-root';
  root.innerHTML =
    '<div id="pcw-card">' +
      '<button id="pcw-x" aria-label="Close">&#x2715;</button>' +
      '<div id="pcw-avatar"><svg xmlns="http://www.w3.org/2000/svg" width="36" height="36" fill="currentColor" viewBox="0 0 16 16"><path d="M8 1a5 5 0 0 0-5 5v1h1a1 1 0 0 1 1 1v3a1 1 0 0 1-1 1H3a1 1 0 0 1-1-1V6a6 6 0 1 1 12 0v6a2.5 2.5 0 0 1-2.5 2.5H9.366a1 1 0 0 1-.866.5h-1a1 1 0 1 1 0-2h1a1 1 0 0 1 .866.5H11.5A1.5 1.5 0 0 0 13 12h-1a1 1 0 0 1-1-1V8a1 1 0 0 1 1-1h1V6a5 5 0 0 0-5-5z"/></svg></div>' +
      '<div id="pcw-name">We Are Here To Help</div>' +
      '<div id="pcw-brand">Page Concrete</div>' +
      '<div id="pcw-body">To Speak With An Experienced, Trusted &amp; Highly Recommended Professional Concrete Team Today!</div>' +
      '<a id="pcw-phone" href="tel:3369627934">' +
        '<svg xmlns="http://www.w3.org/2000/svg" width="14" height="14" fill="currentColor" viewBox="0 0 16 16"><path d="M3.654 1.328a.678.678 0 0 0-1.015-.063L1.605 2.3c-.483.484-.661 1.169-.45 1.77a17.568 17.568 0 0 0 4.168 6.608 17.569 17.569 0 0 0 6.608 4.168c.601.211 1.286.033 1.77-.45l1.034-1.034a.678.678 0 0 0-.063-1.015l-2.307-1.794a.678.678 0 0 0-.58-.122l-2.19.547a1.745 1.745 0 0 1-1.657-.459L5.482 8.062a1.745 1.745 0 0 1-.46-1.657l.548-2.19a.678.678 0 0 0-.122-.58L3.654 1.328z"/></svg>' +
        ' (336) 962-7934' +
      '</a>' +
    '</div>' +
    '<button id="pcw-trigger">' +
      '<svg xmlns="http://www.w3.org/2000/svg" width="15" height="15" fill="currentColor" viewBox="0 0 16 16"><path d="M3.654 1.328a.678.678 0 0 0-1.015-.063L1.605 2.3c-.483.484-.661 1.169-.45 1.77a17.568 17.568 0 0 0 4.168 6.608 17.569 17.569 0 0 0 6.608 4.168c.601.211 1.286.033 1.77-.45l1.034-1.034a.678.678 0 0 0-.063-1.015l-2.307-1.794a.678.678 0 0 0-.58-.122l-2.19.547a1.745 1.745 0 0 1-1.657-.459L5.482 8.062a1.745 1.745 0 0 1-.46-1.657l.548-2.19a.678.678 0 0 0-.122-.58L3.654 1.328z"/></svg>' +
      ' Call Us Today | Free Estimates' +
    '</button>';

  document.body.appendChild(root);

  var card = document.getElementById('pcw-card');
  var trigger = document.getElementById('pcw-trigger');
  var xBtn = document.getElementById('pcw-x');

  setTimeout(function () { card.classList.add('pcw-open'); }, 3000);
  trigger.addEventListener('click', function () { card.classList.toggle('pcw-open'); });
  xBtn.addEventListener('click', function (e) { e.stopPropagation(); card.classList.remove('pcw-open'); });
})();

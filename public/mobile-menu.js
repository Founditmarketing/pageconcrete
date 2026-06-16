/* Mobile menu: clones the desktop nav into #et_mobile_nav_menu (Divi normally
   does this at runtime), wires the hamburger toggle, and adds caret toggles
   to collapsed submenus. */
(function () {
  // Build the mobile dropdown by cloning desktop nav items once.
  function buildMobileMenu() {
    var nav = document.getElementById('et_mobile_nav_menu');
    var mobileNav = nav && nav.querySelector('.mobile_nav');
    var desktopMenu = document.getElementById('top-menu');
    if (!nav || !mobileNav || !desktopMenu || mobileNav.querySelector('.et_mobile_menu')) return;

    var mobileMenu = document.createElement('ul');
    mobileMenu.className = 'et_mobile_menu';
    for (var i = 0; i < desktopMenu.children.length; i++) {
      mobileMenu.appendChild(desktopMenu.children[i].cloneNode(true));
    }
    mobileNav.appendChild(mobileMenu);
  }

  // Toggle open/closed when the hamburger is tapped.
  function initHamburger() {
    var bar = document.querySelector('#et_mobile_nav_menu .mobile_menu_bar');
    if (!bar || bar._hamburgerInited) return;
    bar._hamburgerInited = true;

    bar.addEventListener('click', function () {
      var mobileNav = document.querySelector('#et_mobile_nav_menu .mobile_nav');
      if (!mobileNav) return;
      var isOpen = mobileNav.classList.contains('opened');
      mobileNav.classList.toggle('closed', isOpen);
      mobileNav.classList.toggle('opened', !isOpen);
    });
  }

  // Add caret toggles to parent items in the mobile dropdown.
  function decorate(menu) {
    var parents = menu.querySelectorAll('li.menu-item-has-children');
    for (var i = 0; i < parents.length; i++) {
      var li = parents[i];
      if (li.querySelector(':scope > .submenu-toggle')) continue;
      var link = li.querySelector(':scope > a');
      var sub = li.querySelector(':scope > ul');
      if (!link || !sub) continue;

      var toggle = document.createElement('span');
      toggle.className = 'submenu-toggle';
      toggle.setAttribute('role', 'button');
      toggle.setAttribute('aria-label', 'Toggle submenu');
      li.appendChild(toggle);

      (function (item) {
        toggle.addEventListener('click', function (e) {
          e.preventDefault();
          e.stopPropagation();
          item.classList.toggle('submenu-open');
        });
      })(li);

      if ((link.getAttribute('href') || '').replace(/^.*#/, '#') === '#') {
        (function (item) {
          link.addEventListener('click', function (e) {
            e.preventDefault();
            item.classList.toggle('submenu-open');
          });
        })(li);
      }
    }
  }

  function scan() {
    var menus = document.querySelectorAll('#et_mobile_nav_menu .et_mobile_menu');
    for (var i = 0; i < menus.length; i++) decorate(menus[i]);
  }

  var observer = new MutationObserver(scan);
  observer.observe(document.documentElement, { childList: true, subtree: true });

  function init() {
    buildMobileMenu();
    initHamburger();
    scan();
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', init);
  } else {
    init();
  }
})();

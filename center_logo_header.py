#!/usr/bin/env python3
"""Center the logo in the header:
- Insert the logo as a menu item in the middle of #top-menu (desktop split-menu look)
- Insert a mobile-only Free Quote button before #et-top-navigation
Styling lives in src/custom.css (logo li hidden on mobile, standalone
logo_container hidden on desktop).
"""
import glob

LOGO_LI = ('<li class="menu-item logo-menu-item"><a href="/">'
           '<img src="https://pageconcretenc.com/wp-content/uploads/2024/01/logo.png" '
           'alt="Page Concrete and Outdoor Services" /></a></li>\n')

SERVICE_AREA_LI = '<li class="menu-item menu-item-type-post_type menu-item-object-page menu-item-has-children menu-item-57">'

MOBILE_BTN = '<a href="/contact.html" class="mobile-quote-btn">Free Quote</a>\n\t\t\t\t\t'
TOP_NAV_DIV = '<div id="et-top-navigation"'

files = sorted(f for f in glob.glob('*.html') if not f.startswith('live_'))
stats = {'logo_li': 0, 'mobile_btn': 0}

for path in files:
    with open(path, encoding='utf-8') as fh:
        html = fh.read()
    orig = html

    if 'logo-menu-item' not in html and html.count(SERVICE_AREA_LI) == 1:
        html = html.replace(SERVICE_AREA_LI, LOGO_LI + SERVICE_AREA_LI, 1)
        stats['logo_li'] += 1

    if 'mobile-quote-btn' not in html and html.count(TOP_NAV_DIV) == 1:
        html = html.replace(TOP_NAV_DIV, MOBILE_BTN + TOP_NAV_DIV, 1)
        stats['mobile_btn'] += 1

    if html != orig:
        with open(path, 'w', encoding='utf-8') as fh:
            fh.write(html)

print(f'{len(files)} files scanned, {stats}')

#!/usr/bin/env python3
"""Apply client-requested edits from the 2026-06 review call across all pages:
- Restructure top nav (Residential Concrete / Commercial / Other Services /
  Service Area dropdowns, no "Projects" labels, Get A Free Quote CTA)
- Link /src/custom.css on every page
- Remove stale "Ann Marie: 336-442-6481" phone button
- Fix footer address: Highpoint, NC 27012 -> High Point, NC 27265
"""
import glob
import re

NEW_MENU = '''<ul id="top-menu" class="nav"><li class="menu-item menu-item-type-post_type menu-item-object-page menu-item-home current-menu-item page_item page-item-2 current_page_item menu-item-48"><a href="/" aria-current="page">Home</a></li>
<li class="menu-item menu-item-type-custom menu-item-object-custom menu-item-has-children menu-item-residential-concrete"><a href="#">Residential Concrete</a>
<ul class="sub-menu">
    <li class="menu-item"><a href="/driveway-projects.html">Driveways</a></li>
    <li class="menu-item"><a href="/walkway-projects.html">Walkways &amp; Sidewalks</a></li>
    <li class="menu-item"><a href="/patio-projects.html">Patios</a></li>
    <li class="menu-item"><a href="/step-projects.html">Steps</a></li>
    <li class="menu-item"><a href="/stamped-concrete-projects.html">Stamped Concrete</a></li>
</ul>
</li>
<li class="menu-item menu-item-type-post_type menu-item-object-page"><a href="/commercial-projects.html">Commercial Concrete</a></li>
<li class="menu-item menu-item-type-custom menu-item-object-custom menu-item-has-children menu-item-other-services"><a href="#">Other Services</a>
<ul class="sub-menu">
    <li class="menu-item"><a href="/fencing-projects.html">Fencing</a></li>
    <li class="menu-item"><a href="/deck-projects.html">Decks</a></li>
    <li class="menu-item"><a href="/outdoor-structure-projects.html">Outdoor Structures</a></li>
</ul>
</li>
<li class="menu-item menu-item-type-post_type menu-item-object-page menu-item-has-children menu-item-57"><a href="/service-area.html">Service Area</a>
<ul class="sub-menu">
    <li class="menu-item"><a href="/high-point.html">High Point</a></li>
    <li class="menu-item"><a href="/greensboro.html">Greensboro</a></li>
    <li class="menu-item"><a href="/winston-salem.html">Winston-Salem</a></li>
    <li class="menu-item"><a href="/kernersville.html">Kernersville</a></li>
    <li class="menu-item"><a href="/thomasville.html">Thomasville</a></li>
    <li class="menu-item"><a href="/oak-ridge.html">Oak Ridge</a></li>
    <li class="menu-item"><a href="/summerfield.html">Summerfield</a></li>
    <li class="menu-item"><a href="/clemmons.html">Clemmons</a></li>
    <li class="menu-item"><a href="/archdale.html">Archdale</a></li>
    <li class="menu-item"><a href="/colfax.html">Colfax</a></li>
    <li class="menu-item"><a href="/jamestown.html">Jamestown</a></li>
    <li class="menu-item"><a href="/lexington.html">Lexington</a></li>
    <li class="menu-item"><a href="/midway.html">Midway</a></li>
    <li class="menu-item"><a href="/trinity.html">Trinity</a></li>
    <li class="menu-item"><a href="/union-cross.html">Union Cross</a></li>
    <li class="menu-item"><a href="/walkertown.html">Walkertown</a></li>
    <li class="menu-item"><a href="/walburg.html">Wallburg</a></li>
</ul>
</li>
<li class="menu-item menu-item-type-post_type menu-item-object-page menu-item-62"><a href="/testimonials.html">Testimonials</a></li>
<li class="menu-item menu-item-type-post_type menu-item-object-page menu-item-53"><a href="/faqs.html">FAQs</a></li>
<li class="menu-item menu-item-type-post_type menu-item-object-page menu-item-cta menu-item-50"><a href="/contact.html" class="free-quote-btn">Get A Free Quote</a></li>
</ul>'''

MENU_RE = re.compile(r'<ul id="top-menu" class="nav">.*?</ul>(?=\s*</nav>)', re.DOTALL)

ANN_MARIE_RE = re.compile(
    r'<a href="tel:3369627934" class="service-btn">Derek: 336-962-7934</a>\s*'
    r'<a href="tel:3364426481" class="service-btn">Ann Marie: 336-442-6481</a>'
)
SINGLE_BTN = '<a href="tel:3369627934" class="service-btn">Call For A Free Estimate: 336-962-7934</a>'

CSS_LINK = '<link rel="stylesheet" href="/src/custom.css">\n'

files = sorted(f for f in glob.glob('*.html') if not f.startswith('live_'))
stats = {'menu': 0, 'css': 0, 'annmarie': 0, 'zip': 0}

for path in files:
    with open(path, encoding='utf-8') as fh:
        html = fh.read()
    orig = html

    html, n = MENU_RE.subn(NEW_MENU, html)
    stats['menu'] += n

    if '/src/custom.css' not in html and '</head>' in html:
        html = html.replace('</head>', CSS_LINK + '</head>', 1)
        stats['css'] += 1

    html, n = ANN_MARIE_RE.subn(SINGLE_BTN, html)
    stats['annmarie'] += n

    n = html.count('Highpoint, NC 27012')
    html = html.replace('Highpoint, NC 27012', 'High Point, NC 27265')
    stats['zip'] += n

    if html != orig:
        with open(path, 'w', encoding='utf-8') as fh:
            fh.write(html)
        print(f'updated {path}')

print(stats)

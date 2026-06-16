#!/usr/bin/env python3
"""Replace the mobile header "Free Quote" text button with a form icon.
The .mobile-quote-btn is display:none on desktop, so this is mobile-only.
"""
import glob

OLD = '<a href="/contact.html" class="mobile-quote-btn">Free Quote</a>'
NEW = ('<a href="/contact.html" class="mobile-quote-btn" aria-label="Get a free quote">'
       '<svg viewBox="0 0 24 24" fill="currentColor" aria-hidden="true">'
       '<path d="M19 3h-4.18C14.4 1.84 13.3 1 12 1c-1.3 0-2.4.84-2.82 2H5c-1.1 0-2 .9-2 2'
       'v14c0 1.1.9 2 2 2h14c1.1 0 2-.9 2-2V5c0-1.1-.9-2-2-2zm-7 0c.55 0 1 .45 1 1s-.45 1-1 1'
       '-1-.45-1-1 .45-1 1-1zm2 14H7v-2h7v2zm3-4H7v-2h10v2zm0-4H7V7h10v2z"/></svg></a>')

count = 0
for path in sorted(f for f in glob.glob('*.html') if not f.startswith('live_')):
    with open(path, encoding='utf-8') as fh:
        html = fh.read()
    if OLD in html:
        html = html.replace(OLD, NEW)
        with open(path, 'w', encoding='utf-8') as fh:
            fh.write(html)
        count += 1

print(f'updated {count} files')

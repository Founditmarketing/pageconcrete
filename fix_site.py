import os
import glob
import re

# 1. Text Fixes
for file in glob.glob('*.html'):
    if file.startswith('live_'): continue
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Text replacements
    content = content.replace('Page Concrete', 'Page Concrete and Outdoor Services')
    content = content.replace('Page Concrete and Outdoor Services and Outdoor Services', 'Page Concrete and Outdoor Services')
    
    content = content.replace('3500 psi', '4000 psi')
    content = content.replace('25 plus years', '30 years experience')
    content = content.replace('25 Years', '30 years')
    
    with open(file, 'w', encoding='utf-8') as f:
        f.write(content)

# 2. Contact Info Fixes
for filepath in glob.glob('*.html') + glob.glob('*.py'):
    if filepath.startswith('live_') or filepath == 'fix_site.py': continue
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    original = content
    content = content.replace('336-410-4225', '336-962-7934')
    content = content.replace('3364104225', '3369627934')
    content = content.replace('nacinc4@gmail.com', 'info@pageconcretenc.com')
    
    if content != original:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)

# 3. Menu Restructure
with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Replace the old menus with the new Our Work dropdown
new_menu = """<li class="menu-item menu-item-type-custom menu-item-object-custom menu-item-has-children menu-item-our-work"><a href="#">Our Work</a>
<ul class="sub-menu">
    <li class="menu-item"><a href="/driveway-projects.html">Driveway Projects</a></li>
    <li class="menu-item"><a href="/walkway-projects.html">Walkway Projects</a></li>
    <li class="menu-item"><a href="/patio-projects.html">Patio Projects</a></li>
    <li class="menu-item"><a href="/step-projects.html">Step Projects</a></li>
    <li class="menu-item"><a href="/stamped-concrete-projects.html">Stamped Concrete Projects</a></li>
    <li class="menu-item"><a href="/commercial-projects.html">Commercial Projects</a></li>
    <li class="menu-item"><a href="/fencing-projects.html">Fencing Projects</a></li>
    <li class="menu-item"><a href="/deck-projects.html">Deck Projects</a></li>
    <li class="menu-item"><a href="/outdoor-structure-projects.html">Outdoor Structure Projects</a></li>
</ul>
</li>"""

# We'll use regex to remove Residential Concrete, Commercial, and Gallery LIs and insert new_menu where Residential was
# Residential Concrete
html = re.sub(r'<li class="menu-item menu-item-type-custom menu-item-object-custom menu-item-has-children menu-item-44"><a href="#">Residential Concrete</a>.*?</ul>\n\t\t\t\t\t</li>', new_menu, html, flags=re.DOTALL)
# Commercial
html = re.sub(r'<li class="menu-item menu-item-type-post_type menu-item-object-page menu-item-49"><a href="/commercial\.html">Commercial</a></li>', '', html)
# Gallery
html = re.sub(r'<li class="menu-item menu-item-type-custom menu-item-object-custom menu-item-has-children menu-item-45"><a href="#">Gallery</a>.*?</ul>\n\t\t\t\t\t</li>', '', html, flags=re.DOTALL)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("Text, Contact, and Menu fixed!")

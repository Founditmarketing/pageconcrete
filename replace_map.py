import os
import glob

# HTML to search for (we'll look for a snippet that matches the iframe)
# Since the iframe is on one line:
iframe_search = '<iframe src="https://www.google.com/maps/embed?pb=!1m14!1m8!1m3!1d3339717.720738496!2d-79.86097!3d35.1705075!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x885308f31d2b61a7%3A0xdd25e8706de3e6bf!2sPage%20Concrete!5e0!3m2!1sen!2sus!4v1705953740379!5m2!1sen!2sus" width="2000" height="350" style="border:0;" allowfullscreen="" loading="lazy" referrerpolicy="no-referrer-when-downgrade"></iframe>'

# What we want to replace it with:
replacement_html = """
<div id="footer-map" style="width: 100%; height: 350px; z-index: 1;"></div>
<link rel="stylesheet" href="https://unpkg.com/leaflet@1.9.4/dist/leaflet.css" />
<script src="https://unpkg.com/leaflet@1.9.4/dist/leaflet.js"></script>
<script type="module" src="/footer-map.js"></script>
"""

html_files = glob.glob('*.html')
count = 0

for file_path in html_files:
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()
    
    if iframe_search in content:
        content = content.replace(iframe_search, replacement_html)
        with open(file_path, 'w', encoding='utf-8') as file:
            file.write(content)
        print(f"Updated {file_path}")
        count += 1

print(f"Done! Replaced map in {count} files.")

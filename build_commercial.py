import re
import glob

# Read index.html for template (header and footer)
with open('index.html', 'r', encoding='utf-8') as f:
    template = f.read()

start_marker = '<div id="main-content">'
end_marker = '<footer class="et-l et-l--footer">'

start_idx = template.find(start_marker)
end_idx = template.find(end_marker)

header_html = template[:start_idx + len(start_marker)]
footer_html = template[template.rfind('</div>', 0, end_idx) : ]

# Read live_commercial.html for content
with open('live_commercial.html', 'r', encoding='utf-8') as f:
    live = f.read()

live_start_idx = live.find(start_marker)
live_end_idx = live.find(end_marker)

content = live[live_start_idx + len(start_marker) : live.rfind('</div>', 0, live_end_idx)]

commercial_html = header_html + content + footer_html

with open('commercial.html', 'w', encoding='utf-8') as f:
    f.write(commercial_html)

# Update all links across all files
files = glob.glob('*.html')
for file in files:
    with open(file, 'r', encoding='utf-8') as f:
        file_content = f.read()
    
    file_content = file_content.replace('href="https://pageconcretenc.com/commercial/"', 'href="/commercial.html"')
    
    with open(file, 'w', encoding='utf-8') as f:
        f.write(file_content)

print("commercial.html built successfully and links updated.")

import re
from bs4 import BeautifulSoup

with open('live_commercial.html', 'r', encoding='utf-8') as f:
    html = f.read()

soup = BeautifulSoup(html, 'html.parser')

sections = soup.find_all('div', class_='et_pb_section')

# Parse Hero Section
hero_section = sections[0]
hero_title = hero_section.find(['h1', 'h2']).text.strip()
hero_text = hero_section.find('div', class_='et_pb_text_inner').find_all('p')[-1].text.strip()
hero_btn = hero_section.find('a', class_='et_pb_button')
hero_btn_text = hero_btn.text.strip() if hero_btn else "Contact Us"
hero_btn_href = hero_btn['href'] if hero_btn else "#"

# Parse Gallery Sections
galleries_data = []
for sec in sections[1:]:
    h2 = sec.find('h2')
    if not h2: continue
    title = h2.text.strip()
    
    # Try to find description text
    desc = ""
    texts = sec.find_all('div', class_='et_pb_text_inner')
    for t in texts:
        if t.find('h2'): continue
        if t.text.strip():
            desc = t.text.strip()
            break
            
    images = []
    gallery_items = sec.find_all('div', class_='et_pb_gallery_item')
    for item in gallery_items:
        img = item.find('img')
        if img and img.has_attr('src'):
            src = img['src']
            # if we have high res link, use it for lightbox or just image
            a_tag = item.find('a')
            if a_tag and a_tag.has_attr('href'):
                src = a_tag['href']
            images.append(src)
            
    # Sometimes it's just individual images not a gallery module
    if not gallery_items:
        img_tags = sec.find_all('img')
        for img in img_tags:
            if img.has_attr('src'):
                src = img['src']
                images.append(src)
                
    if title and images:
        galleries_data.append({
            'title': title,
            'desc': desc,
            'images': images
        })

# Now generate the clean HTML
css = """
<style>
.commercial-page {
    font-family: Open Sans, Arial, sans-serif;
    color: #666;
}
.commercial-hero {
    background-color: #eef3fc;
    padding: 60px 20px;
    text-align: left;
}
.commercial-hero-content {
    max-width: 1080px;
    margin: 0 auto;
}
.commercial-hero h1 {
    color: #333;
    font-size: 26px;
    font-weight: bold;
    margin-bottom: 20px;
    line-height: 1.4;
}
.commercial-hero p {
    font-size: 15px;
    line-height: 1.7;
    margin-bottom: 30px;
    max-width: 900px;
}
.commercial-btn {
    display: inline-block;
    background-color: #142ea7;
    color: #fff !important;
    padding: 10px 20px;
    border-radius: 5px;
    font-size: 17px;
    font-weight: 600;
    text-decoration: none;
    transition: background-color 0.3s;
}
.commercial-btn:hover {
    background-color: #006edd;
}

.commercial-section {
    max-width: 1080px;
    margin: 0 auto;
    padding: 60px 20px; /* Increased vertical padding to separate sections */
}
.commercial-section h2 {
    color: #0047ab;
    font-size: 22px;
    font-weight: bold;
    margin-bottom: 10px;
}
.commercial-section p {
    font-size: 15px;
    margin-bottom: 30px;
}
.commercial-grid {
    display: flex;
    flex-wrap: wrap;
    gap: 30px; /* Gap between images */
}
.commercial-grid img {
    width: 220px;
    height: 150px;
    object-fit: cover;
    border: 1px solid #ddd;
    border-radius: 3px;
    box-shadow: 0 2px 5px rgba(0,0,0,0.1);
}

@media (max-width: 980px) {
    .commercial-grid img {
        width: calc(50% - 15px);
    }
}
@media (max-width: 480px) {
    .commercial-grid img {
        width: 100%;
    }
}

.sticky-call-btn {
    position: fixed;
    bottom: 20px;
    right: 20px;
    background-color: #e31818;
    color: #fff !important;
    padding: 12px 20px;
    border-radius: 30px;
    font-size: 16px;
    font-weight: bold;
    box-shadow: 0 4px 10px rgba(0,0,0,0.3);
    z-index: 9999;
    text-decoration: none;
    display: flex;
    align-items: center;
    gap: 10px;
    transition: transform 0.2s;
}
.sticky-call-btn:hover {
    transform: scale(1.05);
}
</style>
"""

html_out = f"""
<div class="commercial-page">
    <div class="commercial-hero">
        <div class="commercial-hero-content">
            <h1>{hero_title}</h1>
            <p>{hero_text}</p>
            <a href="{hero_btn_href}" class="commercial-btn">{hero_btn_text}</a>
        </div>
    </div>
"""

for sec in galleries_data:
    html_out += f"""
    <div class="commercial-section">
        <h2>{sec['title']}</h2>
        <p>{sec['desc']}</p>
        <div class="commercial-grid">
"""
    for img in sec['images']:
        html_out += f'            <img src="{img}" alt="Commercial Concrete Project" />\n'
        
    html_out += """
        </div>
    </div>
"""

html_out += """
    <!-- Sticky Call Button -->
    <a href="tel:336-962-7934" class="sticky-call-btn">
        <i class="icon-phone"></i> Call Us Today | Free Estimates
    </a>
</div>
"""

# Read index.html for template
with open('index.html', 'r', encoding='utf-8') as f:
    template = f.read()

start_marker = '<div id="main-content">'
end_marker = '<footer class="et-l et-l--footer">'

start_idx = template.find(start_marker)
end_idx = template.find(end_marker)

header_html = template[:start_idx + len(start_marker)]
footer_html = template[template.rfind('</div>', 0, end_idx) : ]

# Inject CSS into head
head_end_idx = header_html.find('</head>')
header_html = header_html[:head_end_idx] + css + header_html[head_end_idx:]

final_html = header_html + html_out + footer_html

with open('commercial.html', 'w', encoding='utf-8') as f:
    f.write(final_html)

print("Generated clean commercial.html")

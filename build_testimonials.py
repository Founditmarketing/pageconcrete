import re
from bs4 import BeautifulSoup

with open('live_testimonials.html', 'r', encoding='utf-8') as f:
    html = f.read()

soup = BeautifulSoup(html, 'html.parser')

blurbs = soup.find_all('div', class_='et_pb_blurb')

reviews = []
for blurb in blurbs:
    name_tag = blurb.find('h4', class_='et_pb_module_header')
    desc_tag = blurb.find('div', class_='et_pb_blurb_description')
    if name_tag and desc_tag:
        reviews.append({
            'name': name_tag.text.strip(),
            'content': ''.join(str(c) for c in desc_tag.contents).strip()
        })

css = """
<style>
.testimonials-page {
    font-family: Open Sans, Arial, sans-serif;
    color: #666;
    background-color: #fff;
    padding-bottom: 80px;
}
.testimonials-hero {
    background-color: #eef3fc;
    padding: 80px 20px;
    text-align: center;
}
.testimonials-hero-content {
    max-width: 1080px;
    margin: 0 auto;
    display: flex;
    justify-content: space-between;
    align-items: center;
}
.testimonials-hero h1 {
    color: #333;
    font-size: 26px;
    font-weight: bold;
    margin: 0;
}
.testimonials-btn {
    display: inline-block;
    background-color: #142ea7;
    color: #fff !important;
    padding: 10px 20px;
    border-radius: 5px;
    font-size: 16px;
    font-weight: 600;
    text-decoration: none;
    transition: background-color 0.3s;
}
.testimonials-btn:hover {
    background-color: #006edd;
}

@media (max-width: 768px) {
    .testimonials-hero-content {
        flex-direction: column;
        gap: 20px;
    }
}

.testimonials-section {
    max-width: 1080px;
    margin: 60px auto 0;
    padding: 0 20px;
    text-align: center;
}
.testimonials-section h2 {
    color: #333;
    font-size: 24px;
    font-weight: bold;
    margin-bottom: 20px;
}

.elfsight-widgets {
    margin: 40px auto 60px;
}

.masonry-grid {
    column-count: 3;
    column-gap: 20px;
    max-width: 1080px;
    margin: 0 auto;
    padding: 0 20px;
}
.masonry-item {
    break-inside: avoid;
    background: #f9f9f9;
    padding: 30px;
    margin-bottom: 20px;
    border-radius: 5px;
    text-align: left;
    position: relative;
}
.masonry-item::before {
    content: "❞";
    font-family: Arial, sans-serif;
    font-size: 40px;
    color: #142ea7;
    position: absolute;
    top: 20px;
    left: 20px;
    line-height: 1;
}
.masonry-item h4 {
    color: #333;
    font-size: 18px;
    font-weight: bold;
    margin: 0 0 15px 40px;
}
.masonry-item .review-content {
    font-size: 14px;
    line-height: 1.6;
    color: #555;
    margin-left: 40px;
}
.masonry-item .review-content img {
    max-width: 100%;
    height: auto;
    margin-top: 15px;
    display: block;
}

@media (max-width: 980px) {
    .masonry-grid {
        column-count: 2;
    }
}
@media (max-width: 600px) {
    .masonry-grid {
        column-count: 1;
    }
}
</style>
"""

html_out = f"""
<div class="testimonials-page">
    <div class="testimonials-hero">
        <div class="testimonials-hero-content">
            <h1>Testimonials</h1>
            <a href="/contact.html" class="testimonials-btn">Contact Us</a>
        </div>
    </div>

    <div class="testimonials-section">
        <h2>See What Our Customers Have Been Saying</h2>
        <div class="elfsight-widgets">
            <div class="elfsight-app-86d90f4c-8666-4136-a7ef-b41b58c87118" data-elfsight-app-lazy></div>
        </div>
    </div>

    <div class="testimonials-section">
        <h2>What our customers say</h2>
        <div class="elfsight-widgets">
            <div class="elfsight-app-d1707484-71f0-4aa8-9bf7-e9a9d4438801" data-elfsight-app-lazy></div>
        </div>
    </div>

    <div class="masonry-grid">
"""

for review in reviews:
    html_out += f"""
        <div class="masonry-item">
            <h4>{review['name']}</h4>
            <div class="review-content">
                {review['content']}
            </div>
        </div>
"""

html_out += """
    </div>
</div>
<!-- Elfsight scripts -->
<script src="https://static.elfsight.com/platform/platform.js" data-use-service-core defer></script>
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

# Replace "commercial" active link to "testimonials"
header_html = header_html.replace('current-menu-item"><a href="/commercial.html"', '"><a href="/commercial.html"')
header_html = header_html.replace('"><a href="/testimonials.html"', 'current-menu-item"><a href="/testimonials.html"')

# Inject CSS into head
head_end_idx = header_html.find('</head>')
header_html = header_html[:head_end_idx] + css + header_html[head_end_idx:]

final_html = header_html + html_out + footer_html

with open('testimonials.html', 'w', encoding='utf-8') as f:
    f.write(final_html)

print("Generated clean testimonials.html")

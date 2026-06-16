import re
from bs4 import BeautifulSoup

# Read live site HTML
with open('live_service_area.html', 'r', encoding='utf-8') as f:
    html = f.read()

soup = BeautifulSoup(html, 'html.parser')

# Extract main SEO text
text_modules = soup.find_all('div', class_='et_pb_text_inner')
seo_text_html = ""
for text in text_modules:
    if 'Concrete Contractor Company: Expert Solutions' in text.text:
        # Get the inner HTML
        seo_text_html = ''.join(str(c) for c in text.contents)
        break

# Extract the map iframes
iframes = soup.find_all('iframe')
map_src = ""
for iframe in iframes:
    src = iframe.get('src', '')
    if 'google.com/maps' in src:
        map_src = src
        break

css = """
<style>
.service-page {
    font-family: Open Sans, Arial, sans-serif;
    color: #333;
    background-color: #fff;
    padding-bottom: 80px;
}
.service-hero {
    background-color: #eef3fc;
    padding: 60px 20px;
}
.service-hero-content {
    max-width: 1080px;
    margin: 0 auto;
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    text-align: center;
    width: 100%;
}
.service-hero h1 {
    color: #333;
    font-size: 30px;
    font-weight: bold;
    margin: 0;
}
.service-hero-buttons {
    display: flex;
    justify-content: center;
    align-items: center;
    gap: 20px;
    margin-top: 20px;
    flex-wrap: wrap;
}
.service-btn {
    display: inline-block;
    background-color: #142ea7;
    color: #fff !important;
    padding: 12px 24px;
    border-radius: 5px;
    font-size: 15px;
    font-weight: 600;
    text-decoration: none;
    transition: background-color 0.3s;
}
.service-btn:hover {
    background-color: #006edd;
}

@media (max-width: 768px) {
    .service-hero-content {
        flex-direction: column;
        gap: 30px;
        text-align: center;
    }
    .service-hero-buttons {
        flex-direction: column;
        gap: 15px;
    }
}

.service-section {
    max-width: 1080px;
    margin: 80px auto 0;
    padding: 0 20px;
}



/* Map & Locations */
.map-section {
    text-align: center;
    margin-top: 80px;
}
.map-section h2 {
    font-size: 24px;
    font-weight: bold;
    margin-bottom: 30px;
}
.map-container iframe {
    width: 100%;
    height: 400px;
    border: none;
    border-radius: 5px;
}
.locations-grid {
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    gap: 30px;
    margin-top: 40px;
    text-align: left;
}
.location-item {
    display: flex;
    align-items: center;
    gap: 15px;
    font-size: 16px;
    font-weight: bold;
}
.location-item i {
    color: #142ea7;
    font-size: 24px;
}
@media (max-width: 768px) {
    .locations-grid {
        grid-template-columns: 1fr;
    }
}

/* SEO Content */
.seo-content {
    margin-top: 80px;
    color: #444;
    line-height: 1.8;
}
.seo-content h3 {
    color: #333;
    font-size: 22px;
    margin: 30px 0 15px;
}
.seo-content ul {
    padding-left: 20px;
}
.seo-content li {
    margin-bottom: 10px;
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
<div class="service-page">
    <div class="service-hero">
        <div class="service-hero-content">
            <h1>Service Area</h1>
            <div class="service-hero-buttons">
                <a href="tel:3369627934" class="service-btn">Derek: 336-962-7934</a>
                <a href="tel:3364426481" class="service-btn">Ann Marie: 336-442-6481</a>
            </div>
        </div>
    </div>



    <div class="service-section seo-content">
        {seo_text_html}
    </div>

    <div class="service-section map-section">
        <h2>Located in High Point NC, and service in the surrounding areas.</h2>
        
        <div class="locations-grid">
            <div class="location-item">
                <i class="icon-location"></i> <a href="/high-point.html" style="color:inherit; text-decoration:underline;">High Point, NC</a>
            </div>
            <div class="location-item">
                <i class="icon-location"></i> <a href="/winston-salem.html" style="color:inherit; text-decoration:underline;">Winston Salem, NC</a>
            </div>
            <div class="location-item">
                <i class="icon-location"></i> <a href="/greensboro.html" style="color:inherit; text-decoration:underline;">Greensboro, NC</a>
            </div>
            <div class="location-item">
                <i class="icon-location"></i> <a href="/kernersville.html" style="color:inherit; text-decoration:underline;">Kernersville, NC</a>
            </div>
            <div class="location-item">
                <i class="icon-location"></i> <a href="/thomasville.html" style="color:inherit; text-decoration:underline;">Thomasville, NC</a>
            </div>
            <div class="location-item">
                <i class="icon-location"></i> <a href="/oak-ridge.html" style="color:inherit; text-decoration:underline;">Oak Ridge, NC</a>
            </div>
            <div class="location-item">
                <i class="icon-location"></i> <a href="/summerfield.html" style="color:inherit; text-decoration:underline;">Summerfield, NC</a>
            </div>
            <div class="location-item">
                <i class="icon-location"></i> <a href="/clemmons.html" style="color:inherit; text-decoration:underline;">Clemmons, NC</a>
            </div>
            <div class="location-item">
                <i class="icon-location"></i> <a href="/lexington.html" style="color:inherit; text-decoration:underline;">Lexington, NC</a>
            </div>
            <div class="location-item">
                <i class="icon-location"></i> <a href="/colfax.html" style="color:inherit; text-decoration:underline;">Colfax, NC</a>
            </div>
            <div class="location-item">
                <i class="icon-location"></i> <a href="/archdale.html" style="color:inherit; text-decoration:underline;">Archdale, NC</a>
            </div>
            <div class="location-item">
                <i class="icon-location"></i> <a href="/jamestown.html" style="color:inherit; text-decoration:underline;">Jamestown, NC</a>
            </div>
            <div class="location-item">
                <i class="icon-location"></i> <a href="/walkertown.html" style="color:inherit; text-decoration:underline;">Walkertown, NC</a>
            </div>
            <div class="location-item">
                <i class="icon-location"></i> <a href="/walburg.html" style="color:inherit; text-decoration:underline;">Walburg, NC</a>
            </div>
            <div class="location-item">
                <i class="icon-location"></i> <a href="/trinity.html" style="color:inherit; text-decoration:underline;">Trinity, NC</a>
            </div>
            <div class="location-item">
                <i class="icon-location"></i> <a href="/union-cross.html" style="color:inherit; text-decoration:underline;">Union Cross, NC</a>
            </div>
            <div class="location-item">
                <i class="icon-location"></i> <a href="/midway.html" style="color:inherit; text-decoration:underline;">Midway, NC</a>
            </div>
        </div>
    </div>

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

# Replace active link for service-area
header_html = header_html.replace('current-menu-item"><a href="/"', '"><a href="/"')
header_html = header_html.replace('"><a href="/service-area.html"', 'current-menu-item"><a href="/service-area.html"')

# Inject CSS into head
head_end_idx = header_html.find('</head>')
header_html = header_html[:head_end_idx] + css + header_html[head_end_idx:]

final_html = header_html + html_out + footer_html

with open('service-area.html', 'w', encoding='utf-8') as f:
    f.write(final_html)

print("Generated clean service-area.html")

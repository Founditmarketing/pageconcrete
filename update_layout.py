import os

# 1. Update src/services.css
with open('src/services.css', 'r', encoding='utf-8') as f:
    css = f.read()

if '.service-hero-buttons' not in css:
    css += """

.service-hero-content {
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    text-align: center;
    width: 100%;
}

.service-hero-buttons {
    display: flex;
    justify-content: center;
    align-items: center;
    gap: 15px;
    margin-top: 20px;
    flex-wrap: wrap;
}
"""
    with open('src/services.css', 'w', encoding='utf-8') as f:
        f.write(css)

# 2. Update service-area.html (and we'll let build_city_pages.py handle the rest)
with open('service-area.html', 'r', encoding='utf-8') as f:
    html = f.read()

# The map section starts with <div class="service-section map-section"> and ends with </div> right before <div class="service-section seo-content">
import re
map_pattern = re.compile(r'(<div class="service-section map-section">.*?</div>\s*)(?=<div class="service-section seo-content">)', re.DOTALL)

match = map_pattern.search(html)
if match:
    map_section = match.group(1)
    # Remove from original location
    html = html.replace(map_section, '')
    
    # Insert after seo-content
    seo_end_pattern = re.compile(r'(<div class="service-section seo-content">.*?</div>\s*)(?=<!-- Sticky Call Button -->)', re.DOTALL)
    seo_match = seo_end_pattern.search(html)
    if seo_match:
        html = html.replace(seo_match.group(1), seo_match.group(1) + map_section)

with open('service-area.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("Layout updated!")

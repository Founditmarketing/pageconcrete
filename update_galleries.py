import json
import re

with open('scraped_galleries_unique.json', 'r') as f:
    data = json.load(f)

def generate_gallery_html(images, alt_prefix):
    html = '<div class="gallery-grid">\n'
    for i, img_src in enumerate(images, 1):
        html += f'            <img src="{img_src}" alt="{alt_prefix} {i}" loading="lazy" />\n'
    html += '        </div>'
    return html

file_map = {
    'build_driveway_projects.py': ('driveways', 'Driveway Project'),
    'build_patio_projects.py': ('patios', 'Patio Project'),
    'build_stamped_concrete_projects.py': ('stamped-concrete', 'Stamped Concrete Project'),
    'build_walkway_projects.py': ('sidewalks', 'Walkway Project'),
    'build_commercial_projects.py': ('commercial', 'Commercial Project'),
    'build_deck_projects.py': ('outdoor-services', 'Deck Project'),
    'build_fencing_projects.py': ('outdoor-services', 'Fencing Project'),
    'build_step_projects.py': ('outdoor-services', 'Step Project'),
    'build_outdoor_structure_projects.py': ('outdoor-services', 'Outdoor Structure Project')
}

for filename, (key, alt_prefix) in file_map.items():
    images = data.get(key, [])
    if not images:
        print(f"Skipping {filename}, no images found for {key}.")
        continue
    
    gallery_html = generate_gallery_html(images, alt_prefix)
    
    with open(filename, 'r') as f:
        content = f.read()
    
    pattern = r'<div class="gallery-grid">.*?</div>'
    new_content = re.sub(pattern, gallery_html, content, flags=re.DOTALL)
    
    with open(filename, 'w') as f:
        f.write(new_content)
    
    print(f"Updated {filename} with {len(images)} images.")

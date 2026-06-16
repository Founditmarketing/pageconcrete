import os
import re

files = [
    'build_driveway_projects.py',
    'build_patio_projects.py',
    'build_stamped_concrete_projects.py',
    'build_walkway_projects.py',
    'build_commercial_projects.py',
    'build_deck_projects.py',
    'build_fencing_projects.py',
    'build_step_projects.py',
    'build_outdoor_structure_projects.py'
]

for filename in files:
    if not os.path.exists(filename):
        continue
        
    with open(filename, 'r') as f:
        content = f.read()

    # Remove the map section
    map_pattern = r'<section class="service-map-placeholder">.*?</section>'
    content = re.sub(map_pattern, '', content, flags=re.DOTALL)
    
    # Remove the sticky call button
    button_pattern = r'<!-- Sticky Call Button -->\s*<a[^>]*class="sticky-call-btn"[^>]*>.*?</a>'
    content = re.sub(button_pattern, '', content, flags=re.DOTALL)
    
    with open(filename, 'w') as f:
        f.write(content)
        
    print(f"Removed duplicates from {filename}")

import json
import re

with open('scraped_galleries_unique.json', 'r') as f:
    data = json.load(f)

outdoor_images = data.get('outdoor-services', [])
if not outdoor_images:
    print("No outdoor images found.")
    exit()

# Format as Python list of strings for the script
img_list_str = '[\n    ' + ',\n    '.join([f"'{img}'" for img in outdoor_images]) + '\n]'

files_to_update = [
    'build_deck_projects.py',
    'build_fencing_projects.py',
    'build_step_projects.py',
    'build_outdoor_structure_projects.py'
]

pattern = r"for img in \[[^\]]*\]:"
replacement = f"for img in {img_list_str}:"

for filename in files_to_update:
    with open(filename, 'r') as f:
        content = f.read()
    
    new_content = re.sub(pattern, replacement, content)
    
    with open(filename, 'w') as f:
        f.write(new_content)
    print(f"Updated {filename} with {len(outdoor_images)} images.")

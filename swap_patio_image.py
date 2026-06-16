import json
import glob
import os

old_img = 'https://pageconcretenc.com/wp-content/uploads/2024/01/walnut5.jpg'
new_img = 'https://pageconcretenc.com/wp-content/uploads/2024/02/new-residentail-backyward-patio-in-NC.jpg'

# 1. Update HTML files
html_files = glob.glob('*.html')
for file in html_files:
    with open(file, 'r', encoding='utf-8') as f:
        html = f.read()
    
    if old_img in html:
        html = html.replace(old_img, new_img)
        with open(file, 'w', encoding='utf-8') as f:
            f.write(html)
        print(f"Updated {file}")

# 2. Update JSON
with open('scraped_galleries_unique.json', 'r') as f:
    data = json.load(f)

# Put old image back into patios
if old_img not in data['patios']:
    data['patios'].append(old_img)

# Remove new image from patios
if new_img in data['patios']:
    data['patios'].remove(new_img)

with open('scraped_galleries_unique.json', 'w') as f:
    json.dump(data, f, indent=4)

print("Swapped patio image in HTML and JSON")

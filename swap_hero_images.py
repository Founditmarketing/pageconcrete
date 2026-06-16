import json

# 1. Update index.html
with open('index.html', 'r') as f:
    html = f.read()

replacements = {
    'https://pageconcretenc.com/wp-content/uploads/2024/01/patios-image.jpg': 'https://pageconcretenc.com/wp-content/uploads/2024/01/walnut5.jpg',
    'https://pageconcretenc.com/wp-content/uploads/2024/01/driveways-image.jpg': 'https://pageconcretenc.com/wp-content/uploads/2024/01/2.jpg',
    'https://pageconcretenc.com/wp-content/uploads/2024/01/sidewalks-image.jpg': 'https://pageconcretenc.com/wp-content/uploads/2024/01/42_1.jpg',
    'https://pageconcretenc.com/wp-content/uploads/2024/01/stampede-concrete-image.jpg': 'https://pageconcretenc.com/wp-content/uploads/2024/01/46_1.jpg'
}

for old, new in replacements.items():
    html = html.replace(old, new)

with open('index.html', 'w') as f:
    f.write(html)

# 2. Update scraped_galleries_unique.json to remove these 4 images
with open('scraped_galleries_unique.json', 'r') as f:
    data = json.load(f)

for cat in data:
    data[cat] = [img for img in data[cat] if img not in replacements.values()]

with open('scraped_galleries_unique.json', 'w') as f:
    json.dump(data, f, indent=4)

print("Images swapped in index.html and removed from scraped_galleries_unique.json")

import json
import urllib.request
import os
from PIL import Image, ImageDraw, ImageFont
import math

with open('scraped_galleries.json', 'r') as f:
    data = json.load(f)

urls = data['patios']
images = []
labels = []

os.makedirs('temp_patios', exist_ok=True)

for i, url in enumerate(urls):
    filename = url.split('/')[-1]
    filepath = os.path.join('temp_patios', filename)
    try:
        if not os.path.exists(filepath):
            req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
            with urllib.request.urlopen(req) as response, open(filepath, 'wb') as out_file:
                out_file.write(response.read())
        
        img = Image.open(filepath)
        img = img.convert('RGB')
        img.thumbnail((300, 300))
        images.append(img)
        labels.append(filename)
    except Exception as e:
        print(f"Failed to load {filename}: {e}")

if not images:
    print("No images loaded")
    exit()

cols = 5
rows = math.ceil(len(images) / cols)
w, h = 300, 320 # 20px for text

montage = Image.new('RGB', (cols * w, rows * h), (255, 255, 255))
draw = ImageDraw.Draw(montage)

for i, img in enumerate(images):
    x = (i % cols) * w
    y = (i // cols) * h
    
    # paste image
    montage.paste(img, (x, y + 20))
    
    # draw text
    draw.text((x + 5, y + 5), labels[i], fill=(0, 0, 0))

montage.save('montage.jpg')
print("Saved montage.jpg")

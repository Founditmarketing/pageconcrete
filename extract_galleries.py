import urllib.request
from bs4 import BeautifulSoup
import json
import ssl

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

urls = {
    'driveways': 'https://pageconcretenc.com/driveways-gallery/',
    'patios': 'https://pageconcretenc.com/patios-gallery/',
    'stamped-concrete': 'https://pageconcretenc.com/stamped-concrete-gallery/',
    'sidewalks': 'https://pageconcretenc.com/sidewalks-gallery/',
    'outdoor-services': 'https://pageconcretenc.com/outdoor-services/'
}

results = {}
headers = {'User-Agent': 'Mozilla/5.0'}

for name, url in urls.items():
    print(f"Fetching {name}...")
    try:
        req = urllib.request.Request(url, headers=headers)
        with urllib.request.urlopen(req, context=ctx, timeout=10) as response:
            html = response.read()
            
        soup = BeautifulSoup(html, 'html.parser')
        
        gallery_items = soup.find_all('div', class_='et_pb_gallery_image')
        images = []
        for item in gallery_items:
            img = item.find('img')
            if img and img.has_attr('src'):
                src = img.get('src')
                a_tag = item.find('a')
                if a_tag and a_tag.has_attr('href') and (a_tag['href'].endswith('.jpg') or a_tag['href'].endswith('.png')):
                    src = a_tag['href']
                
                src = src.split('?')[0]
                if src not in images:
                    images.append(src)
        
        results[name] = images
        print(f"  Found {len(images)} images for {name}.")
    except Exception as e:
        print(f"Error fetching {name}: {e}")

with open('scraped_galleries.json', 'w') as f:
    json.dump(results, f, indent=4)

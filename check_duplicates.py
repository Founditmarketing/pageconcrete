import json
import os

with open('scraped_galleries.json', 'r') as f:
    data = json.load(f)

for key, images in data.items():
    # extract filenames without extensions and -scaled
    basenames = []
    unique_images = []
    duplicates = []
    for img in images:
        basename = os.path.basename(img)
        # remove query params
        basename = basename.split('?')[0]
        # remove -scaled or other suffixes
        basename = basename.replace('-scaled', '')
        # remove dimensions like -400x284
        import re
        basename = re.sub(r'-\d+x\d+', '', basename)
        
        if basename in basenames:
            duplicates.append(img)
        else:
            basenames.append(basename)
            unique_images.append(img)
    
    print(f"[{key}] total: {len(images)}, unique: {len(unique_images)}, duplicates: {len(duplicates)}")
    if duplicates:
        print(f"  Duplicates found: {duplicates}")
        
    data[key] = unique_images

with open('scraped_galleries_unique.json', 'w') as f:
    json.dump(data, f, indent=4)


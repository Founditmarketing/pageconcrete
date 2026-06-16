import glob

replacements = {
    'https://pageconcretenc.com/wp-content/uploads/2024/01/patios-image.jpg': 'https://pageconcretenc.com/wp-content/uploads/2024/01/walnut5.jpg',
    'https://pageconcretenc.com/wp-content/uploads/2024/01/driveways-image.jpg': 'https://pageconcretenc.com/wp-content/uploads/2024/01/2.jpg',
    'https://pageconcretenc.com/wp-content/uploads/2024/01/sidewalks-image.jpg': 'https://pageconcretenc.com/wp-content/uploads/2024/01/42_1.jpg',
    'https://pageconcretenc.com/wp-content/uploads/2024/01/stampede-concrete-image.jpg': 'https://pageconcretenc.com/wp-content/uploads/2024/01/46_1.jpg'
}

html_files = glob.glob('*.html')
for file in html_files:
    with open(file, 'r', encoding='utf-8') as f:
        html = f.read()
    
    modified = False
    for old, new in replacements.items():
        if old in html:
            html = html.replace(old, new)
            modified = True
            
    if modified:
        with open(file, 'w', encoding='utf-8') as f:
            f.write(html)
        print(f"Updated {file}")

print("Done swapping images in all HTML files.")

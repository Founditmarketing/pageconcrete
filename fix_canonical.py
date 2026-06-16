import glob

files = glob.glob('*.html')

for file in files:
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()

    # Fix canonical links pointing to directory
    content = content.replace('<link rel="canonical" href="/" />', '<link rel="canonical" href="https://pageconcretenc.com/" />')
    
    with open(file, 'w', encoding='utf-8') as f:
        f.write(content)

print("Fixed canonical links")

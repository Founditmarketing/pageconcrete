import glob

files = glob.glob('*.html') + glob.glob('*.py') + glob.glob('*.js')

for file_path in files:
    if file_path == 'rename_company.py': continue
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()
    
    if 'Page Concrete' in content:
        content = content.replace('Page Concrete', 'Page Concrete and Outdoor Services')
        with open(file_path, 'w', encoding='utf-8') as file:
            file.write(content)
        print(f"Updated {file_path}")
print("Done!")

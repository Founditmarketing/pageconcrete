import os
import glob

files_to_check = glob.glob('*.html') + glob.glob('*.py')

for filepath in files_to_check:
    if filepath == 'update_contact.py' or filepath == 'fix_site.py' or filepath.startswith('live_'):
        continue
        
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
        
    original = content
    # Replace various phone formats
    content = content.replace('(336) 410-4225', '336-962-7934')
    content = content.replace('336-410-4225', '336-962-7934')
    content = content.replace('3364104225', '3369627934')
    # Replace email
    content = content.replace('nacinc4@gmail.com', 'info@pageconcretenc.com')
    
    if content != original:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Updated {filepath}")

print("Done updating contact info.")

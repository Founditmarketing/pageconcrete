import os
import glob

files = glob.glob('*.html') + glob.glob('*.py')

for filepath in files:
    if filepath == 'update_contact_info.py':
        continue
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
        
    original = content
    content = content.replace('336-962-7934', '336-962-7934')
    content = content.replace('3369627934', '3369627934')
    content = content.replace('info@pageconcretenc.com', 'info@pageconcretenc.com')
    
    if content != original:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Updated {filepath}")

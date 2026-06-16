import os

files = ['build_patio_projects.py', 'build_patios.py']

for file in files:
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Replace the class prefixes
    content = content.replace('class="patios-', 'class="service-')
    
    with open(file, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print(f"Updated classes in {file}")

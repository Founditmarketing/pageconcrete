import sys

def replace_links(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    content = content.replace('https://pageconcretenc.com/patios/', '/patios.html')
    
    if file_path == 'patios.html':
        if '<link rel="stylesheet" href="/src/patios.css">' not in content:
            content = content.replace('</head>', '\t<link rel="stylesheet" href="/src/patios.css">\n</head>')
            
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)

replace_links('index.html')
replace_links('patios.html')
print("Links updated")

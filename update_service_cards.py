import glob

html_files = glob.glob('*.html')

for file in html_files:
    with open(file, 'r', encoding='utf-8') as f:
        html = f.read()
    
    modified = False
    
    replacements = {
        'href="/patios.html"': 'href="/patio-projects.html"',
        'href="/driveways.html"': 'href="/driveway-projects.html"',
        'href="/sidewalks.html"': 'href="/walkway-projects.html"',
        'href="/stamped-concrete.html"': 'href="/stamped-concrete-projects.html"',
        '<h3> Sidewalks </h3>': '<h3> Walkways </h3>'
    }
    
    for old, new in replacements.items():
        if old in html:
            html = html.replace(old, new)
            modified = True
            
    if modified:
        with open(file, 'w', encoding='utf-8') as f:
            f.write(html)
        print(f"Updated {file}")

print("Done updating service cards across all HTML files.")

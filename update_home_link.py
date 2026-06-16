import os

files = ['index.html', 'patios.html', 'driveways.html', 'sidewalks.html', 'stamped-concrete.html']

for file in files:
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()

    # Replace the absolute URL with a local relative URL
    content = content.replace('href="https://pageconcretenc.com/"', 'href="/"')

    with open(file, 'w', encoding='utf-8') as f:
        f.write(content)

print("Home links updated.")

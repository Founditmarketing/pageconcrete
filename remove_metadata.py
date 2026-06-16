import re

files = ['index.html', 'patios.html', 'driveways.html', 'sidewalks.html', 'stamped-concrete.html']

for file in files:
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()

    # Use regex to strip anything before <!DOCTYPE html>
    # Find index of <!DOCTYPE
    idx = content.find('<!DOCTYPE html>')
    if idx > 0:
        content = content[idx:]
        with open(file, 'w', encoding='utf-8') as f:
            f.write(content)

print("Metadata removed.")

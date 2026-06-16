import re

files = ['patios.html', 'driveways.html', 'sidewalks.html', 'stamped-concrete.html']

for file in files:
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()

    # Remove the map placeholder section
    content = re.sub(r'<section class="service-map-placeholder">.*?</section>', '', content, flags=re.DOTALL)

    # Remove the sticky call button
    content = re.sub(r'<!-- Sticky Call Button -->\s*<a href="tel:336-962-7934" class="sticky-call-btn">\s*<i class="icon-phone"></i> Call Us Today \| Free Estimates\s*</a>', '', content, flags=re.DOTALL)

    with open(file, 'w', encoding='utf-8') as f:
        f.write(content)

print("Duplicates removed.")

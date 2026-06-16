import os

with open('src/patios.css', 'r') as f:
    css = f.read()

css = css.replace('.patios-', '.service-')
css = css.replace('Patios Page Styles', 'Service Page Styles')

with open('src/services.css', 'w') as f:
    f.write(css)

with open('patios.html', 'r') as f:
    html = f.read()

html = html.replace('patios.css', 'services.css')
html = html.replace('class="patios-', 'class="service-')

with open('patios.html', 'w') as f:
    f.write(html)

os.remove('src/patios.css')
print("Migrated patios.css to services.css")

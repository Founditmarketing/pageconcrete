import glob

replacements = {
    'https://pageconcretenc.com/commercial/': '/commercial.html',
    'https://pageconcretenc.com/commercial': '/commercial.html',
    'https://pageconcretenc.com/testimonials/': '/testimonials.html',
    'https://pageconcretenc.com/testimonials': '/testimonials.html',
    'https://pageconcretenc.com/service-area/': '/service-area.html',
    'https://pageconcretenc.com/service-area': '/service-area.html',
    'https://pageconcretenc.com/contact-us/': '/contact.html',
    'https://pageconcretenc.com/contact-us': '/contact.html',
    'https://pageconcretenc.com/faqs/': '/faqs.html',
    'https://pageconcretenc.com/faqs': '/faqs.html',
    'https://pageconcretenc.com/gallery/': '/gallery.html',
    'https://pageconcretenc.com/gallery': '/gallery.html',
    'https://pageconcretenc.com/driveways-gallery/': '/driveways-gallery.html',
    'https://pageconcretenc.com/driveways-gallery': '/driveways-gallery.html',
    'https://pageconcretenc.com/patios-gallery/': '/patios-gallery.html',
    'https://pageconcretenc.com/patios-gallery': '/patios-gallery.html',
    'https://pageconcretenc.com/stamped-concrete-gallery/': '/stamped-concrete-gallery.html',
    'https://pageconcretenc.com/stamped-concrete-gallery': '/stamped-concrete-gallery.html',
    'https://pageconcretenc.com/sidewalks-gallery/': '/sidewalks-gallery.html',
    'https://pageconcretenc.com/sidewalks-gallery': '/sidewalks-gallery.html',
    'https://pageconcretenc.com/outdoor-services/': '/outdoor-services.html',
    'https://pageconcretenc.com/outdoor-services': '/outdoor-services.html',
}

for file in glob.glob('*.html'):
    if file.startswith('live_'): continue
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    new_content = content
    for old, new in replacements.items():
        new_content = new_content.replace(old, new)
        
    # Also fix active menu item for service-area
    if file == 'service-area.html':
        new_content = new_content.replace('current-menu-item"><a href="/"', '"><a href="/"')
        new_content = new_content.replace('"><a href="/service-area.html"', 'current-menu-item"><a href="/service-area.html"')
        
    if content != new_content:
        with open(file, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f"Fixed {file}")

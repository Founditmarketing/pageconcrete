import glob
import os

head_injection = """
<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/glightbox/dist/css/glightbox.min.css" />
"""

body_injection = """
<script src="https://cdn.jsdelivr.net/npm/glightbox/dist/js/glightbox.min.js"></script>
<script>
document.addEventListener('DOMContentLoaded', function() {
    const gallerySelectors = ['.gallery-grid', '.commercial-grid', '.outdoor-gallery'];
    gallerySelectors.forEach(sel => {
        const containers = document.querySelectorAll(sel);
        containers.forEach(container => {
            const images = container.querySelectorAll('img');
            images.forEach(img => {
                if (img.parentNode.tagName === 'A') {
                    img.parentNode.classList.add('glightbox');
                    img.parentNode.setAttribute('data-gallery', 'gallery');
                } else {
                    const a = document.createElement('a');
                    a.href = img.src;
                    a.classList.add('glightbox');
                    a.setAttribute('data-gallery', 'gallery');
                    img.parentNode.insertBefore(a, img);
                    a.appendChild(img);
                }
            });
        });
    });
    
    if (typeof GLightbox !== 'undefined') {
        const lightbox = GLightbox({
            selector: '.glightbox',
            touchNavigation: true,
            loop: true,
            zoomable: true
        });
    }
});
</script>
"""

html_files = glob.glob('*.html')

for file in html_files:
    with open(file, 'r', encoding='utf-8') as f:
        html = f.read()
    
    modified = False
    
    # Inject into head if not present
    if 'glightbox.min.css' not in html:
        html = html.replace('</head>', head_injection + '\n</head>')
        modified = True
        
    # Inject before body if not present
    if 'glightbox.min.js' not in html:
        html = html.replace('</body>', body_injection + '\n</body>')
        modified = True
        
    if modified:
        with open(file, 'w', encoding='utf-8') as f:
            f.write(html)
        print(f"Added lightbox to {file}")

print("Done adding lightbox to all HTML files.")

import sys

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

start_marker = '<div id="main-content">'
end_marker = '<footer class="et-l et-l--footer">'

start_idx = html.find(start_marker)
end_idx = html.find(end_marker)

header_html = html[:start_idx + len(start_marker)]
footer_html = html[html.rfind('</div>', 0, end_idx) : ]

patios_content = """
<div class="service-page-container">
    <div class="service-hero">
        <h1>Take Your Backyard to the Next Level</h1>
    </div>

    <section class="service-section section-split">
        <div class="service-content-left">
            <h2 class="service-heading-blue">Get Help From A Concrete Patio Installer In High Point, Greensboro, Kernersville, Clemmons, Winston-Salem, And Surrounding Areas In NC</h2>
            <p>Nothing says summer like lounging on the patio with your friends and family. Give yourself a space to spend time outdoors with help from Page Concrete and Outdoor Services. We're a top concrete patio installer in the High Point, Greensboro, Kernersville, Clemmons, Winston-Salem, and surrounding areas in NC.</p>
            <p>When you hire us, we'll:</p>
            <ul>
                <li>Work with you to design the layout of your patio</li>
                <li>Help you choose between stamped concrete or hard finish concrete</li>
                <li>Get to work installing your high-end, beautiful patio</li>
            </ul>
            <p>Stamped concrete can look like other high-end materials, so you can get a low-maintenance patio that looks elegant. Call <a href="tel:336-962-7934">336-962-7934</a> now to speak with a concrete patio installer about your project.</p>
        </div>
        <div class="service-image-right">
            <img src="https://pageconcretenc.com/wp-content/uploads/2024/01/patios-image.jpg" alt="Stamped Concrete Patio" />
        </div>
    </section>

    <section class="service-section section-split">
        <div class="service-content-left">
            <h2 class="service-heading-blue">We Can Repair Your Damaged Patio</h2>
            <p>Can you see cracks in your concrete patio? Is the concrete sunken? Look no further than Page Concrete and Outdoor Services for patio repair services. We'll figure out what's wrong with your patio and fix it as quickly as possible. You'll be enjoying backyard barbecues with friends again in no time.</p>
            <p>If you need concrete patio repair services, get in touch with us today.</p>
            <a href="/patios.html" class="service-btn">Click Here To View Our Patios</a>
        </div>
        <div class="service-image-right">
            <img src="https://pageconcretenc.com/wp-content/uploads/2024/02/new-residentail-backyward-patio-in-NC.jpg" alt="Covered concrete patio" />
        </div>
    </section>

    <section class="service-gallery">
        <div class="gallery-grid">
            <img src="https://pageconcretenc.com/wp-content/uploads/2024/02/new-residentail-backyward-patio-in-NC.jpg" alt="Patio Project 1" />
            <img src="https://pageconcretenc.com/wp-content/uploads/2024/02/new-residentail-patio-install-in-NC.jpg" alt="Patio Project 2" />
            <img src="https://pageconcretenc.com/wp-content/uploads/2024/01/patios-image.jpg" alt="Patio Project 3" />
            <img src="https://pageconcretenc.com/wp-content/uploads/2024/02/new-residentail-patio-install-in-NC.jpg" alt="Patio Project 4" />
        </div>
    </section>

    <section class="service-map-placeholder">
        <iframe src="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d102919.46746401036!2d-80.05779017684074!3d36.08381830606836!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x8853194a2b9fb177%3A0xc3b8aeb716d12f12!2sGreensboro%2C%20NC!5e0!3m2!1sen!2sus!4v1717387345672!5m2!1sen!2sus" width="100%" height="450" style="border:0;" allowfullscreen="" loading="lazy" referrerpolicy="no-referrer-when-downgrade"></iframe>
    </section>
</div>

<!-- Sticky Call Button -->
<a href="tel:336-962-7934" class="sticky-call-btn">
    <i class="icon-phone"></i> Call Us Today | Free Estimates
</a>
"""

new_html = header_html + patios_content + footer_html

new_html = new_html.replace('</head>', '\t<link rel="stylesheet" href="/src/services.css">\n</head>')

# Update the "Patios" link in the menu to point to "/patios.html"
# Find `<a href="https://pageconcretenc.com/patios/" aria-current="page">Patios</a>` or similar
# Let's just do a generic replace for the URL:
new_html = new_html.replace('href="https://pageconcretenc.com/patios/"', 'href="/patios.html"')

with open('patios.html', 'w', encoding='utf-8') as f:
    f.write(new_html)

print("Generated patios.html successfully.")

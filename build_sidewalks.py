import sys

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

start_marker = '<div id="main-content">'
end_marker = '<footer class="et-l et-l--footer">'

start_idx = html.find(start_marker)
end_idx = html.find(end_marker)

header_html = html[:start_idx + len(start_marker)]
footer_html = html[html.rfind('</div>', 0, end_idx) : ]

sidewalks_content = """
<div class="service-page-container">
    <div class="service-hero">
        <h1>New Concrete Sidewalk Install Services</h1>
    </div>

    <section class="service-section section-split">
        <div class="service-content-left">
            <h2 class="service-heading-blue">Schedule Concrete Sidewalk Installation Services In High Point, Greensboro, Kernersville, Clemmons, Winston-Salem, And Surrounding Areas In NC</h2>
            <p>Do you want to add an elegant walkway leading to your front door? Do you want to replace the cracked sidewalk in front of your property? Homeowners in High Point, Greensboro, Kernersville, Clemmons, Winston-Salem, and surrounding areas in NC turn to Page Concrete and Outdoor Services for concrete sidewalk installation services. Our crew has the skills and tools needed to install a durable concrete sidewalk on your property.</p>
            <p>You can choose between a regular gray concrete sidewalk or a stamped concrete sidewalk. Stamped concrete sidewalks will look more high-end and enhance the appearance of your property.</p>
            <p>Call <a href="tel:336-962-7934">336-962-7934</a> now to speak with a residential sidewalk installer.</p>
            
            <br>

            <h2 class="service-heading-blue" style="margin-top: 20px;">What Else Can We Do For You?</h2>
            <p>You can count on Page Concrete and Outdoor Services for more than just concrete sidewalk installation services. We can also install durable concrete stairs and landings. We know how to install nearly any concrete feature.</p>
            <p>Contact a residential sidewalk installer today to set up an appointment.</p>
            <a href="/sidewalks.html" class="service-btn" style="margin-top: 15px;">Click Here To View Our Sidewalks</a>
        </div>
        <div class="service-image-right" style="display: flex; align-items: stretch;">
            <img src="https://pageconcretenc.com/wp-content/uploads/2024/01/sidewalks-image.jpg" alt="Concrete Sidewalk" style="object-fit: cover; height: 100%; min-height: 500px;" />
        </div>
    </section>

    <section class="service-gallery">
        <div class="gallery-grid">
            <img src="https://pageconcretenc.com/wp-content/uploads/2024/01/sidewalks-image.jpg" alt="Sidewalk Project 1" />
            <img src="https://pageconcretenc.com/wp-content/uploads/2024/02/concrete-work-residential-in-NC.jpg" alt="Sidewalk Project 2" />
            <img src="https://pageconcretenc.com/wp-content/uploads/2024/01/sidewalks-image.jpg" alt="Sidewalk Project 3" />
            <img src="https://pageconcretenc.com/wp-content/uploads/2024/02/concrete-work-residential-in-NC.jpg" alt="Sidewalk Project 4" />
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

new_html = header_html + sidewalks_content + footer_html

new_html = new_html.replace('</head>', '\t<link rel="stylesheet" href="/src/services.css">\n</head>')
new_html = new_html.replace('https://pageconcretenc.com/driveways/', '/driveways.html')
new_html = new_html.replace('https://pageconcretenc.com/patios/', '/patios.html')
new_html = new_html.replace('https://pageconcretenc.com/sidewalks/', '/sidewalks.html')

with open('sidewalks.html', 'w', encoding='utf-8') as f:
    f.write(new_html)

def replace_links(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    content = content.replace('https://pageconcretenc.com/sidewalks/', '/sidewalks.html')
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)

replace_links('index.html')
replace_links('patios.html')
replace_links('driveways.html')

print("Generated sidewalks.html successfully and updated links.")

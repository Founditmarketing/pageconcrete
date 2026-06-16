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
            <img src="https://pageconcretenc.com/wp-content/uploads/2024/01/11.jpg" alt="Walkway Project 1" loading="lazy" />
            <img src="https://pageconcretenc.com/wp-content/uploads/2024/01/12.jpg" alt="Walkway Project 2" loading="lazy" />
            <img src="https://pageconcretenc.com/wp-content/uploads/2024/01/5.jpg" alt="Walkway Project 3" loading="lazy" />
            <img src="https://pageconcretenc.com/wp-content/uploads/2024/01/1610722615981_20210114_131740_1_-scaled.jpg" alt="Walkway Project 4" loading="lazy" />
            <img src="https://pageconcretenc.com/wp-content/uploads/2024/01/20201022_151631__sidewalk_and_stamp_concrete_1.jpg" alt="Walkway Project 5" loading="lazy" />
            <img src="https://pageconcretenc.com/wp-content/uploads/2024/01/susan-cocke-steps.jpg" alt="Walkway Project 6" loading="lazy" />
            <img src="https://pageconcretenc.com/wp-content/uploads/2024/01/14_3.jpg" alt="Walkway Project 7" loading="lazy" />
            <img src="https://pageconcretenc.com/wp-content/uploads/2024/01/12_3.jpg" alt="Walkway Project 8" loading="lazy" />
            <img src="https://pageconcretenc.com/wp-content/uploads/2024/01/11_3.jpg" alt="Walkway Project 9" loading="lazy" />
            <img src="https://pageconcretenc.com/wp-content/uploads/2024/01/8_1.jpg" alt="Walkway Project 10" loading="lazy" />
            <img src="https://pageconcretenc.com/wp-content/uploads/2024/01/20_1.jpg" alt="Walkway Project 11" loading="lazy" />
        </div>
    </section>

    
</div>


"""

new_html = header_html + sidewalks_content + footer_html

new_html = new_html.replace('</head>', '\t<link rel="stylesheet" href="/src/services.css">\n</head>')
new_html = new_html.replace('https://pageconcretenc.com/driveways/', '/driveways.html')
new_html = new_html.replace('https://pageconcretenc.com/patios/', '/patios.html')
new_html = new_html.replace('https://pageconcretenc.com/sidewalks/', '/sidewalks.html')

with open('walkway-projects.html', 'w', encoding='utf-8') as f:
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

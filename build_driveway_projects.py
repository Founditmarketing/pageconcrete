import sys

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

start_marker = '<div id="main-content">'
end_marker = '<footer class="et-l et-l--footer">'

start_idx = html.find(start_marker)
end_idx = html.find(end_marker)

header_html = html[:start_idx + len(start_marker)]
footer_html = html[html.rfind('</div>', 0, end_idx) : ]

driveways_content = """
<div class="service-page-container">
    <div class="service-hero">
        <h1>Need a Wider Driveway for Multiple Cars?</h1>
        <p style="max-width: 800px; margin: 20px auto; font-size: 1.1rem; color: #555;">A concrete driveway is a durable and practical choice for any commercial or residential property. Its strength, long lifespan, and minimal maintenance make it a popular option among property owners. At Page Concrete and Outdoor Services, we specialize in expert concrete driveway installations that provide lasting value and enhance the curb appeal of your property. If you need a new driveway or an extension we are the right team to get the job done the first time.</p>
        <a href="/contact.html" class="service-btn" style="margin-top: 20px;">Contact Concrete Driveway Company</a>
    </div>

    <section class="service-section section-split">
        <div class="service-content-left">
            <h2 class="service-heading-blue">Arrange For Driveway Extension Services In High Point, Greensboro, Kernersville, Clemmons, Winston-Salem, And Surrounding Areas In NC</h2>
            <p>If you need more parking space in front of your home, turn to Page Concrete and Outdoor Services for help. We provide driveway extension services for residential clients in the High Point, Greensboro, Kernersville, Clemmons, Winston-Salem, and surrounding areas in NC. We'll use high-quality concrete and professional-grade equipment to create a driveway that looks great and will last for years. We can also add walkways around your property.</p>
            <p>Call <a href="tel:336-962-7934">336-962-7934</a> now to get more information about our driveway extension services.</p>
        </div>
        <div class="service-image-right">
            <img src="https://pageconcretenc.com/wp-content/uploads/2024/02/new-residentail-driveway-install-in-NC.jpg" alt="Driveway Extension" />
        </div>
    </section>

    <section class="service-section section-split">
        <div class="service-content-left">
            <h2 class="service-heading-blue">When Should You Replace Your Driveway?</h2>
            <p>Page Concrete and Outdoor Services specializes in driveway replacement services. You should replace your old driveway if...</p>
            <ul>
                <li>Your driveway is damaged and looks worse for wear</li>
                <li>You want to improve the appearance of your property</li>
                <li>You have a gravel driveway and want to switch to concrete</li>
            </ul>
            <p>We can even use stamped or stained concrete to complement your home's exterior. We use high-end Brickform products. To schedule driveway replacement services, email us today.</p>
            <a href="/driveways.html" class="service-btn">Click Here To View Our Driveways</a>
        </div>
        <div class="service-image-right">
            <img src="https://pageconcretenc.com/wp-content/uploads/2024/01/driveways-image.jpg" alt="Damaged Driveway" />
        </div>
    </section>

    <section class="service-gallery">
        <div class="gallery-grid">
            <img src="https://pageconcretenc.com/wp-content/uploads/2024/01/1611348950257_20201210_142942_driveway_121420.jpg" alt="Driveway Project 1" loading="lazy" />
            <img src="https://pageconcretenc.com/wp-content/uploads/2024/01/1611348941553_20201211_141313_driveway_121420.jpg" alt="Driveway Project 2" loading="lazy" />
            <img src="https://pageconcretenc.com/wp-content/uploads/2024/01/33_1.jpg" alt="Driveway Project 3" loading="lazy" />
            <img src="https://pageconcretenc.com/wp-content/uploads/2024/02/new-residentail-driveway-install-in-NC-1.jpg" alt="Driveway Project 4" loading="lazy" />
            <img src="https://pageconcretenc.com/wp-content/uploads/2024/01/3a.jpg" alt="Driveway Project 5" loading="lazy" />
            <img src="https://pageconcretenc.com/wp-content/uploads/2024/01/20200928_180800__driveway_1.jpg" alt="Driveway Project 6" loading="lazy" />
            <img src="https://pageconcretenc.com/wp-content/uploads/2024/01/40_1.jpg" alt="Driveway Project 7" loading="lazy" />
            <img src="https://pageconcretenc.com/wp-content/uploads/2024/01/Large_Driveway_Extension_2.jpg" alt="Driveway Project 8" loading="lazy" />
            <img src="https://pageconcretenc.com/wp-content/uploads/2024/01/22_1.jpg" alt="Driveway Project 9" loading="lazy" />
            <img src="https://pageconcretenc.com/wp-content/uploads/2024/01/7_1.jpg" alt="Driveway Project 10" loading="lazy" />
            <img src="https://pageconcretenc.com/wp-content/uploads/2024/01/Large_Driveway_Extension.jpg" alt="Driveway Project 11" loading="lazy" />
            <img src="https://pageconcretenc.com/wp-content/uploads/2024/01/31.jpg" alt="Driveway Project 12" loading="lazy" />
            <img src="https://pageconcretenc.com/wp-content/uploads/2024/01/3_1.jpg" alt="Driveway Project 13" loading="lazy" />
            <img src="https://pageconcretenc.com/wp-content/uploads/2024/01/35_1.jpg" alt="Driveway Project 14" loading="lazy" />
            <img src="https://pageconcretenc.com/wp-content/uploads/2024/01/6_1.jpg" alt="Driveway Project 15" loading="lazy" />
            <img src="https://pageconcretenc.com/wp-content/uploads/2024/01/4_1.jpg" alt="Driveway Project 16" loading="lazy" />
            <img src="https://pageconcretenc.com/wp-content/uploads/2024/01/23_1.jpg" alt="Driveway Project 17" loading="lazy" />
        </div>
    </section>

    
</div>


"""

new_html = header_html + driveways_content + footer_html

new_html = new_html.replace('</head>', '\t<link rel="stylesheet" href="/src/services.css">\n</head>')
new_html = new_html.replace('https://pageconcretenc.com/driveways/', '/driveways.html')
new_html = new_html.replace('https://pageconcretenc.com/patios/', '/patios.html')

with open('driveway-projects.html', 'w', encoding='utf-8') as f:
    f.write(new_html)

def replace_links(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    content = content.replace('https://pageconcretenc.com/driveways/', '/driveways.html')
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)

replace_links('index.html')
replace_links('patios.html')

print("Generated driveways.html successfully and updated links.")

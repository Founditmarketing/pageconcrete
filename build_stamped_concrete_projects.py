import sys

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

start_marker = '<div id="main-content">'
end_marker = '<footer class="et-l et-l--footer">'

start_idx = html.find(start_marker)
end_idx = html.find(end_marker)

header_html = html[:start_idx + len(start_marker)]
footer_html = html[html.rfind('</div>', 0, end_idx) : ]

stamped_content = """
<div class="service-page-container">
    <div class="service-hero">
        <h1>Stamped Concrete Installation Services</h1>
    </div>

    <section class="service-section section-split">
        <div class="service-content-left">
            <h2 class="service-heading-blue">Rely On Us For Stamped Concrete Installation Services In High Point, Greensboro, Kernersville, Clemmons, Winston-Salem, And Surrounding Areas In NC</h2>
            <p>When you think of concrete, do you think of a boring, gray slab? That's about to change. Stamped concrete is a beautiful option that can take any concrete feature to the next level. Page Concrete and Outdoor Services can install stamped concrete patios, driveways, walkways, sidewalks and stairs for homeowners in and around High Point, Greensboro, Kernersville, Clemmons, Winston-Salem, and surrounding areas in NC.</p>
            <p>Stamped concrete isn't just beautiful-it's also low-maintenance. You can expect your concrete feature to last for years.</p>
            <p>Call <a href="tel:336-962-7934">336-962-7934</a> now to arrange for stamped concrete installation services.</p>
            
            <br>

            <h2 class="service-heading-blue" style="margin-top: 20px;">Learn More About Stamped Concrete</h2>
            <p>One of the best features of stamped concrete is that it can mimic the look of other, more expensive materials, such as:</p>
            <ul>
                <li>Brick</li>
                <li>Tile</li>
                <li>Natural stone</li>
                <li>Slate</li>
                <li>Cobblestone</li>
                <li>Flagstone</li>
            </ul>
            <p>You'll pay just a fraction of the price of these materials for your stamped concrete installation. If you're interested in a stamped concrete patio, driveway or walkway, reach out to us now.</p>
            <a href="/stamped-concrete.html" class="service-btn" style="margin-top: 15px;">Click Here To View Our Stamped Concrete</a>
        </div>
        <div class="service-image-right" style="display: flex; align-items: stretch;">
            <img src="https://pageconcretenc.com/wp-content/uploads/2024/01/stampede-concrete-image.jpg" alt="Stamped Concrete Pattern" style="object-fit: cover; height: 100%; min-height: 500px;" onerror="this.src='https://pageconcretenc.com/wp-content/uploads/2024/01/1610726485104_stamp_concrete_7.22.20.jpg'" />
        </div>
    </section>

    <section class="service-gallery">
        <div class="gallery-grid">
            <img src="https://pageconcretenc.com/wp-content/uploads/2024/01/stamp_concrete___7.22.20_1.jpg" alt="Stamped Concrete Project 1" loading="lazy" />
            <img src="https://pageconcretenc.com/wp-content/uploads/2024/01/Stamp_Pattern_-_Ashlar_Slate.jpg" alt="Stamped Concrete Project 2" loading="lazy" />
            <img src="https://pageconcretenc.com/wp-content/uploads/2024/01/Stamped_Patio.jpg" alt="Stamped Concrete Project 3" loading="lazy" />
            <img src="https://pageconcretenc.com/wp-content/uploads/2024/01/Stamped_Patio_2.jpg" alt="Stamped Concrete Project 4" loading="lazy" />
            <img src="https://pageconcretenc.com/wp-content/uploads/2024/01/Stamped_Patio_Extension.jpg" alt="Stamped Concrete Project 5" loading="lazy" />
            <img src="https://pageconcretenc.com/wp-content/uploads/2024/01/20200605_075102__patio_and_stamp_concrete_1.jpg" alt="Stamped Concrete Project 6" loading="lazy" />
            <img src="https://pageconcretenc.com/wp-content/uploads/2024/01/20201022_151631__sidewalk_and_stamp_concrete_1.jpg" alt="Stamped Concrete Project 7" loading="lazy" />
            <img src="https://pageconcretenc.com/wp-content/uploads/2024/01/stampede-concrete-image.jpg" alt="Stamped Concrete Project 8" loading="lazy" />
            <img src="https://pageconcretenc.com/wp-content/uploads/2024/01/bricks.jpg" alt="Stamped Concrete Project 9" loading="lazy" />
            <img src="https://pageconcretenc.com/wp-content/uploads/2024/01/9_3.jpg" alt="Stamped Concrete Project 10" loading="lazy" />
            <img src="https://pageconcretenc.com/wp-content/uploads/2024/01/18_3.jpg" alt="Stamped Concrete Project 11" loading="lazy" />
            <img src="https://pageconcretenc.com/wp-content/uploads/2024/01/17_3.jpg" alt="Stamped Concrete Project 12" loading="lazy" />
            <img src="https://pageconcretenc.com/wp-content/uploads/2024/01/slatepattern3.jpg" alt="Stamped Concrete Project 13" loading="lazy" />
            <img src="https://pageconcretenc.com/wp-content/uploads/2024/01/susan-cocke-steps.jpg" alt="Stamped Concrete Project 14" loading="lazy" />
            <img src="https://pageconcretenc.com/wp-content/uploads/2024/01/10_1.jpg" alt="Stamped Concrete Project 15" loading="lazy" />
            <img src="https://pageconcretenc.com/wp-content/uploads/2024/01/11_3.jpg" alt="Stamped Concrete Project 16" loading="lazy" />
            <img src="https://pageconcretenc.com/wp-content/uploads/2024/01/12_3.jpg" alt="Stamped Concrete Project 17" loading="lazy" />
            <img src="https://pageconcretenc.com/wp-content/uploads/2024/01/14_3.jpg" alt="Stamped Concrete Project 18" loading="lazy" />
            <img src="https://pageconcretenc.com/wp-content/uploads/2024/01/15_1.jpg" alt="Stamped Concrete Project 19" loading="lazy" />
            <img src="https://pageconcretenc.com/wp-content/uploads/2024/01/37_1.jpg" alt="Stamped Concrete Project 20" loading="lazy" />
            <img src="https://pageconcretenc.com/wp-content/uploads/2024/01/44_1.jpg" alt="Stamped Concrete Project 21" loading="lazy" />
        </div>
    </section>

    
</div>


"""

new_html = header_html + stamped_content + footer_html

new_html = new_html.replace('</head>', '\t<link rel="stylesheet" href="/src/services.css">\n</head>')
new_html = new_html.replace('https://pageconcretenc.com/driveways/', '/driveways.html')
new_html = new_html.replace('https://pageconcretenc.com/patios/', '/patios.html')
new_html = new_html.replace('https://pageconcretenc.com/sidewalks/', '/sidewalks.html')
new_html = new_html.replace('https://pageconcretenc.com/stamped-concrete/', '/stamped-concrete.html')

with open('stamped-concrete-projects.html', 'w', encoding='utf-8') as f:
    f.write(new_html)

def replace_links(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    content = content.replace('https://pageconcretenc.com/stamped-concrete/', '/stamped-concrete.html')
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)

replace_links('index.html')
replace_links('patios.html')
replace_links('driveways.html')
replace_links('sidewalks.html')

print("Generated stamped-concrete.html successfully and updated links.")

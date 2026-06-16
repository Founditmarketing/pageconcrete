css = """
<style>
.faq-page {
    font-family: Open Sans, Arial, sans-serif;
    color: #333;
    background-color: #fff;
    padding-bottom: 80px;
}
.faq-hero {
    background-color: #eef3fc;
    padding: 60px 20px;
}
.faq-hero-content {
    max-width: 1080px;
    margin: 0 auto;
    display: flex;
    justify-content: space-between;
    align-items: center;
}
.faq-hero h1 {
    color: #333;
    font-size: 30px;
    font-weight: bold;
    margin: 0;
}
.contact-btn {
    display: inline-block;
    background-color: #142ea7;
    color: #fff !important;
    padding: 12px 24px;
    border-radius: 5px;
    font-size: 15px;
    font-weight: 600;
    text-decoration: none;
    transition: background-color 0.3s;
}
.contact-btn:hover {
    background-color: #006edd;
}

@media (max-width: 768px) {
    .faq-hero-content {
        flex-direction: column;
        gap: 20px;
        text-align: left;
        align-items: flex-start;
    }
}

.faq-section {
    max-width: 1080px;
    margin: 60px auto 0;
    padding: 0 20px;
}
.faq-item {
    display: flex;
    gap: 20px;
    margin-bottom: 40px;
    border-bottom: 1px solid #eee;
    padding-bottom: 30px;
}
.faq-item:last-of-type {
    border-bottom: none;
}
.faq-icon {
    flex-shrink: 0;
    width: 24px;
    height: 24px;
    margin-top: 5px;
}
.faq-icon svg {
    width: 100%;
    height: 100%;
    fill: #142ea7;
}
.faq-content h3 {
    font-size: 18px;
    font-weight: bold;
    color: #333;
    margin: 0 0 15px 0;
}
.faq-content p {
    font-size: 14px;
    line-height: 1.6;
    color: #555;
    margin: 0 0 15px 0;
}
.faq-content p:last-child {
    margin-bottom: 0;
}

.faq-footer {
    margin-top: 40px;
}
.contact-btn-large {
    display: inline-block;
    background-color: #142ea7;
    color: #fff !important;
    padding: 14px 30px;
    border-radius: 5px;
    font-size: 16px;
    font-weight: bold;
    text-decoration: none;
    transition: background-color 0.3s;
}
.contact-btn-large:hover {
    background-color: #006edd;
}

.sticky-call-btn {
    position: fixed;
    bottom: 20px;
    right: 20px;
    background-color: #e31818;
    color: #fff !important;
    padding: 12px 20px;
    border-radius: 30px;
    font-size: 16px;
    font-weight: bold;
    box-shadow: 0 4px 10px rgba(0,0,0,0.3);
    z-index: 9999;
    text-decoration: none;
    display: flex;
    align-items: center;
    gap: 10px;
    transition: transform 0.2s;
}
.sticky-call-btn:hover {
    transform: scale(1.05);
}
</style>
"""

svg_icon = '<svg viewBox="0 0 24 24"><path d="M12 2C6.48 2 2 6.48 2 12s4.48 10 10 10 10-4.48 10-10S17.52 2 12 2zm1 17h-2v-2h2v2zm2.07-7.75l-.9.92C13.45 12.9 13 13.5 13 15h-2v-.5c0-1.1.45-2.1 1.17-2.83l1.24-1.26c.37-.36.59-.86.59-1.41 0-1.1-.9-2-2-2s-2 .9-2 2H8c0-2.21 1.79-4 4-4s4 1.79 4 4c0 .88-.36 1.68-.93 2.25z"/></svg>'

html_out = f"""
<div class="faq-page">
    <div class="faq-hero">
        <div class="faq-hero-content">
            <h1>FAQs</h1>
            <a href="/contact.html" class="contact-btn">Contact Us</a>
        </div>
    </div>

    <div class="faq-section">
        <div class="faq-item">
            <div class="faq-icon">{svg_icon}</div>
            <div class="faq-content">
                <h3>What is Cement and Concrete?</h3>
                <p>Cement and concrete often are used interchangeably. However, cement is actually an ingredient of concrete.</p>
                <p>Concrete is a mixture of sand, gravel or crushed stone, a paste of water and Portland Cement.</p>
                <p>Cement comprises from 10 to 15 percent of the concrete mix, by volume. Through a process called hydration, the cement and water harden and bind it all into a rocklike mass. This hardening process continues for years meaning that concrete gets stronger as it gets older.</p>
            </div>
        </div>

        <div class="faq-item">
            <div class="faq-icon">{svg_icon}</div>
            <div class="faq-content">
                <h3>How long does it take for concrete to cure?</h3>
                <p>The concrete will take a full 28 days to cure on its own and fully dry.</p>
            </div>
        </div>

        <div class="faq-item">
            <div class="faq-icon">{svg_icon}</div>
            <div class="faq-content">
                <h3>What is Fibermesh?</h3>
                <p>This is a concrete additive that is mixed in with the cement at the ready mix plant. If you could look at a cross section of Fibermesh fibrous concrete, you would see millions of polypropylene Fibermesh fibers uniformly distributed in all directions throughout the concrete mix. These fibers provide top-to-bottom, side-to-side uniform reinforcement and are a cost-effective and superior alternative to rebar or wire mesh reinforcement. We use Fibermesh in most of our concrete mixtures.</p>
            </div>
        </div>

        <div class="faq-item">
            <div class="faq-icon">{svg_icon}</div>
            <div class="faq-content">
                <h3>How thick should my concrete be poured?</h3>
                <p>Thickness is the major factor (even more than the strength of the concrete) in determining a structural capacity. Concrete is to be poured at a minimum thickness of 4 inches. Increasing the thickness from 4 inches to 5 inches will add approximately 20% to your concrete cost, but will also boost the load-carrying capacity nearly 50%. Depending on the traffic you will have or the weight you intend for the concrete area to be able to withstand, you may want to increase to 6" or 8". We use a minimum thickness of 4 inches unless noted otherwise.</p>
            </div>
        </div>

        <div class="faq-item">
            <div class="faq-icon">{svg_icon}</div>
            <div class="faq-content">
                <h3>Does concrete have to be grey?</h3>
                <p>Not at all. There is an almost limitless palette of special finishes for concrete pavements and slabs. With the addition of color and a skilled decorative concrete contractor, concrete can take on almost any shape, pattern, color or texture, in both exterior and interior applications.</p>
            </div>
        </div>

        <div class="faq-item">
            <div class="faq-icon">{svg_icon}</div>
            <div class="faq-content">
                <h3>How long does it take before I can drive on new driveway?</h3>
                <p>In our market area, the American Concrete Institute and the American Concrete Pavement association recommend a minimum of (7) seven days following concrete placement before using a concrete driveway.</p>
            </div>
        </div>

        <div class="faq-item">
            <div class="faq-icon">{svg_icon}</div>
            <div class="faq-content">
                <h3>How long does it take before I can walk on my new concrete?</h3>
                <p>We recommend not to walk on new concrete for (3) days.</p>
            </div>
        </div>

        <div class="faq-item">
            <div class="faq-icon">{svg_icon}</div>
            <div class="faq-content">
                <h3>Is the process of installing concrete affected by weather?</h3>
                <p>Yes. The rate at which concrete hardens is very much affected by temperature, moisture and wind. Wind can cause the surface to crack. Rain will significantly weaken the surface. Placing concrete in cold weather often involves heating some of the concrete ingredients and protecting the freshly-placed concrete from freezing. Placing concrete in hot weather might mean cooling materials or adding ingredients to slow the curing of the concrete.</p>
            </div>
        </div>

        <div class="faq-item">
            <div class="faq-icon">{svg_icon}</div>
            <div class="faq-content">
                <h3>Will concrete crack?</h3>
                <p>Yes, concrete does crack. To minimize and control cracking, control joints are placed in the concrete so that the concrete cracks where those control joints are placed. These are either hand control joints or a saw cuts. We also add concrete products that contain millions of fibers mixed throughout the concrete to help control cracking even more. There is NO GUARANTEE that concrete will not crack in other places.</p>
            </div>
        </div>

        <div class="faq-item">
            <div class="faq-icon">{svg_icon}</div>
            <div class="faq-content">
                <h3>Is there a recommended on-going maintenance program for my concrete?</h3>
                <p>In addition to sealing concrete every 2-3 years,</p>
                <p>Do not allow rusting metals to set on the concrete.</p>
                <p>Frequent sweeping and occasional hosing will be enough to keep your concrete looking good. Wet leaves on a driveway have a tendency to stain, so be prepared to clean your driveway often in fall.</p>
                <p>Do not allow water to drain beneath the slab. Settlement cracks may develop.</p>
                <p>Do not allow snow and ice to accumulate the first winter. Keep the driveway shoveled off.</p>
                <p>Do not apply deicing chemicals for snow and ice removal the first winter. As an alternative, sand can be used for traction.</p>
                <p>WARNING: Never use deicers containing ammonium sulfate or ammonium nitrate (i.e. fertilizers). Such products are known to aggressively attack concrete.</p>
            </div>
        </div>

        <div class="faq-item">
            <div class="faq-icon">{svg_icon}</div>
            <div class="faq-content">
                <h3>What strength of concrete do we use?</h3>
                <p>4000 psi for patios and sidewalks.</p>
                <p>Add Commercial work and occasional some residential we will use 5000 psi.</p>
                <p>With added fiber reinforcement on all projects.</p>
            </div>
        </div>

        <div class="faq-item">
            <div class="faq-icon">{svg_icon}</div>
            <div class="faq-content">
                <h3>How are concrete and asphalt different?</h3>
                <p>Concrete is more versatile than asphalt because it can be used both outdoors and indoors. For example, you may decide you want a decorative concrete floor inside your commercial building. Asphalt, on the other hand, can only be used for outdoor applications. Concrete lasts longer than asphalt while needing less maintenance. While a concrete driveway can last up to 30 years, an asphalt driveway may only last 12 years. Keep in mind that you'll still need to apply concrete sealer. However, you won't have to seal pavement as often as you would with asphalt. Concrete is not only long-lasting, but durable enough to withstand heavy traffic. Many of our customers appreciate how concrete is durable enough to use on freeways, intersections and other high traffic areas without potholing.</p>
            </div>
        </div>

        <div class="faq-footer">
            <a href="/contact.html" class="contact-btn-large">Contact Us</a>
        </div>
    </div>

    <!-- Sticky Call Button -->
    <a href="tel:336-962-7934" class="sticky-call-btn">
        <i class="icon-phone"></i> Call Us Today | Free Estimates
    </a>
</div>
"""

# Read index.html for template
with open('index.html', 'r', encoding='utf-8') as f:
    template = f.read()

start_marker = '<div id="main-content">'
end_marker = '<footer class="et-l et-l--footer">'

start_idx = template.find(start_marker)
end_idx = template.find(end_marker)

header_html = template[:start_idx + len(start_marker)]
footer_html = template[template.rfind('</div>', 0, end_idx) : ]

# Replace active link for FAQs
header_html = header_html.replace('current-menu-item"><a href="/"', '"><a href="/"')
header_html = header_html.replace('"><a href="/faqs.html"', 'current-menu-item"><a href="/faqs.html"')

# Inject CSS into head
head_end_idx = header_html.find('</head>')
header_html = header_html[:head_end_idx] + css + header_html[head_end_idx:]

# Ensure title is appropriate
header_html = header_html.replace('<title>Concrete Contractor Services In High Point Greensboro Winston Salem</title>', '<title>FAQs - Page Concrete and Outdoor Services</title>')

final_html = header_html + html_out + footer_html

with open('faqs.html', 'w', encoding='utf-8') as f:
    f.write(final_html)

print("Generated faqs.html")

css = """
<style>
.contact-page {
    font-family: Open Sans, Arial, sans-serif;
    color: #333;
    background-color: #fff;
    padding-bottom: 80px;
}
.contact-hero {
    background-color: #eef3fc;
    padding: 60px 20px;
}
.contact-hero-content {
    max-width: 1080px;
    margin: 0 auto;
}
.contact-hero h1 {
    color: #333;
    font-size: 26px;
    font-weight: bold;
    margin: 0;
    line-height: 1.4;
}

.contact-section {
    max-width: 1080px;
    margin: 60px auto 0;
    padding: 0 20px;
    display: flex;
    gap: 60px;
}
.contact-left {
    flex: 1.2;
}
.contact-right {
    flex: 0.8;
}

@media (max-width: 980px) {
    .contact-section {
        flex-direction: column;
        gap: 40px;
    }
}

.contact-left h2 {
    font-size: 26px;
    font-weight: bold;
    color: #333;
    margin-bottom: 20px;
}
.contact-left p {
    font-size: 15px;
    line-height: 1.6;
    margin-bottom: 20px;
    color: #555;
}

/* Form Styles */
.contact-form-container {
    margin-top: 40px;
}
.contact-form-container h3 {
    font-size: 26px;
    font-weight: bold;
    margin-bottom: 10px;
    color: #000;
}
.contact-form-container p.subtitle {
    color: #666;
    margin-bottom: 30px;
    font-size: 14px;
}
.form-row {
    display: flex;
    gap: 20px;
    margin-bottom: 20px;
}
.form-group {
    flex: 1;
    display: flex;
    flex-direction: column;
}
.form-group label {
    font-weight: bold;
    font-size: 14px;
    margin-bottom: 8px;
    color: #000;
}
.form-group input, .form-group textarea {
    padding: 12px;
    border: 1px solid #ccc;
    border-radius: 4px;
    font-family: inherit;
    font-size: 14px;
}
.form-group textarea {
    height: 120px;
    resize: vertical;
}
.form-group .file-upload {
    border: 2px dashed #ccc;
    padding: 30px;
    text-align: center;
    border-radius: 4px;
    color: #666;
    background: #fafafa;
    cursor: pointer;
}
.form-submit {
    text-align: center;
    margin-top: 30px;
}
.submit-btn {
    background-color: #0d8cf8;
    color: #fff;
    border: none;
    padding: 12px 30px;
    font-size: 16px;
    font-weight: bold;
    border-radius: 4px;
    cursor: pointer;
}
.submit-btn:hover {
    background-color: #0077df;
}
.recaptcha-text {
    font-size: 12px;
    color: #888;
    text-align: center;
    margin-top: 15px;
}

/* Contact Info Styles */
.contact-info-list {
    display: flex;
    flex-direction: column;
    gap: 40px;
}
.contact-info-item {
    display: flex;
    gap: 20px;
}
.contact-info-icon {
    width: 24px;
    height: 24px;
    flex-shrink: 0;
}
.contact-info-icon svg {
    width: 100%;
    height: 100%;
    fill: #142ea7;
}
.contact-info-content h4 {
    font-size: 16px;
    font-weight: bold;
    color: #333;
    margin: 0 0 10px 0;
}
.contact-info-content p {
    font-size: 14px;
    color: #555;
    margin: 0 0 5px 0;
    line-height: 1.5;
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

html_out = f"""
<div class="contact-page">
    <div class="contact-hero">
        <div class="contact-hero-content">
            <h1>Find a Concrete Contractor in High Point, Greensboro, Kernersville, Clemmons, Winston-Salem, and surrounding areas in NC</h1>
        </div>
    </div>

    <div class="contact-section">
        <div class="contact-left">
            <h2>Contact Page Concrete and Outdoor Services Today</h2>
            <p>Thank you for visiting the website of Page Concrete and Outdoor Services. We're located in High Point, NC and serve the surrounding areas. If you need residential concrete services, turn to us.</p>
            <p>Please use the form on this page to contact us. You can also call us at 336-962-7934. We look forward to serving you.</p>

            <div class="contact-form-container">
                <h3>Get in touch</h3>
                <p class="subtitle">Leave your message and we'll get back to you shortly.</p>
                
                <form action="#" method="POST">
                    <div class="form-row">
                        <div class="form-group">
                            <label>First Name</label>
                            <input type="text" placeholder="John" name="first_name" />
                        </div>
                        <div class="form-group">
                            <label>Last Name</label>
                            <input type="text" placeholder="Doe" name="last_name" />
                        </div>
                    </div>

                    <div class="form-row">
                        <div class="form-group">
                            <label>Email *</label>
                            <input type="email" placeholder="example@domain.com" name="email" required />
                        </div>
                        <div class="form-group">
                            <label>Phone</label>
                            <input type="tel" placeholder="+1 000 000 0000" name="phone" />
                        </div>
                    </div>

                    <div class="form-group" style="margin-bottom: 20px;">
                        <label>Message *</label>
                        <textarea placeholder="Your questions or comments" name="message" required></textarea>
                    </div>

                    <div class="form-group">
                        <label>Attachments</label>
                        <p style="font-size: 12px; color: #888; margin: 0 0 10px;">Allowed file types: jpg, jpeg, png, gif, txt, pdf, doc, docx, xls, xlsx, odt, ppt, pptx, pps, ppsx, html, and less than 100 MB.</p>
                        <div class="file-upload">
                            <span style="color: #0d8cf8;">Choose file</span> or drop here
                        </div>
                    </div>

                    <div class="form-submit">
                        <button type="submit" class="submit-btn">Submit</button>
                    </div>
                    <p class="recaptcha-text">This site is protected by reCAPTCHA and the Google <a href="#">Privacy Policy</a> and <a href="#">Terms of Service</a> apply.</p>
                </form>
            </div>
        </div>

        <div class="contact-right">
            <div class="contact-info-list">
                <div class="contact-info-item">
                    <div class="contact-info-icon">
                        <svg viewBox="0 0 24 24"><path d="M12 2C8.13 2 5 5.13 5 9c0 5.25 7 13 7 13s7-7.75 7-13c0-3.87-3.13-7-7-7zm0 9.5c-1.38 0-2.5-1.12-2.5-2.5s1.12-2.5 2.5-2.5 2.5 1.12 2.5 2.5-1.12 2.5-2.5 2.5z"/></svg>
                    </div>
                    <div class="contact-info-content">
                        <h4>Page Concrete and Outdoor Services</h4>
                        <p>Highpoint, NC 27012</p>
                    </div>
                </div>

                <div class="contact-info-item">
                    <div class="contact-info-icon">
                        <svg viewBox="0 0 24 24"><path d="M6.62 10.79c1.44 2.83 3.76 5.14 6.59 6.59l2.2-2.2c.27-.27.67-.36 1.02-.24 1.12.37 2.33.57 3.57.57.55 0 1 .45 1 1V20c0 .55-.45 1-1 1-9.39 0-17-7.61-17-17 0-.55.45-1 1-1h3.5c.55 0 1 .45 1 1 0 1.25.2 2.45.57 3.57.11.35.03.74-.25 1.02l-2.2 2.2z"/></svg>
                    </div>
                    <div class="contact-info-content">
                        <h4>Call Us</h4>
                        <p>Phone: 336-962-7934</p>
                    </div>
                </div>

                <div class="contact-info-item">
                    <div class="contact-info-icon">
                        <svg viewBox="0 0 24 24"><path d="M20 4H4c-1.1 0-1.99.9-1.99 2L2 18c0 1.1.9 2 2 2h16c1.1 0 2-.9 2-2V6c0-1.1-.9-2-2-2zm0 4l-8 5-8-5V6l8 5 8-5v2z"/></svg>
                    </div>
                    <div class="contact-info-content">
                        <h4>Email Us</h4>
                        <p>Email: info@pageconcretenc.com</p>
                    </div>
                </div>

                <div class="contact-info-item">
                    <div class="contact-info-icon">
                        <svg viewBox="0 0 24 24"><path d="M11.99 2C6.47 2 2 6.48 2 12s4.47 10 9.99 10C17.52 22 22 17.52 22 12S17.52 2 11.99 2zM12 20c-4.42 0-8-3.58-8-8s3.58-8 8-8 8 3.58 8 8-3.58 8-8 8zm.5-13H11v6l5.25 3.15.75-1.23-4.5-2.67z"/></svg>
                    </div>
                    <div class="contact-info-content">
                        <h4>Hours</h4>
                        <p>Mon-Fri: 8:00am-6:00pm<br>Sat: 8:00am-1:00pm<br>Sun: Closed</p>
                    </div>
                </div>

                <div class="contact-info-item">
                    <div class="contact-info-icon">
                        <svg viewBox="0 0 24 24"><path d="M12 2C8.13 2 5 5.13 5 9c0 5.25 7 13 7 13s7-7.75 7-13c0-3.87-3.13-7-7-7zm0 9.5c-1.38 0-2.5-1.12-2.5-2.5s1.12-2.5 2.5-2.5 2.5 1.12 2.5 2.5-1.12 2.5-2.5 2.5z"/></svg>
                    </div>
                    <div class="contact-info-content">
                        <h4>Additional Locations</h4>
                        <p>High Point, NC 27265<br>Winston Salem, NC 27105<br><br>Kernersville, NC and Surrounding Areas</p>
                    </div>
                </div>
            </div>
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

# Replace active link for contact
header_html = header_html.replace('current-menu-item"><a href="/"', '"><a href="/"')
header_html = header_html.replace('"><a href="/contact.html"', 'current-menu-item"><a href="/contact.html"')

# Inject CSS into head
head_end_idx = header_html.find('</head>')
header_html = header_html[:head_end_idx] + css + header_html[head_end_idx:]

final_html = header_html + html_out + footer_html

with open('contact.html', 'w', encoding='utf-8') as f:
    f.write(final_html)

print("Generated clean contact.html")

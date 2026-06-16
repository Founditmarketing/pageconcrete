import os
import shutil

# 1. Update existing build scripts
def update_script(old_file, new_file, old_html, new_html):
    if os.path.exists(old_file):
        with open(old_file, 'r') as f:
            content = f.read()
        content = content.replace(f"'{old_html}'", f"'{new_html}'")
        content = content.replace(f'"{old_html}"', f'"{new_html}"')
        with open(new_file, 'w') as f:
            f.write(content)

update_script('build_patios.py', 'build_patio_projects.py', 'patios.html', 'patio-projects.html')
update_script('build_driveways.py', 'build_driveway_projects.py', 'driveways.html', 'driveway-projects.html')
update_script('build_sidewalks.py', 'build_walkway_projects.py', 'sidewalks.html', 'walkway-projects.html')
update_script('build_stamped.py', 'build_stamped_concrete_projects.py', 'stamped-concrete.html', 'stamped-concrete-projects.html')
update_script('build_commercial_clean.py', 'build_commercial_projects.py', 'commercial.html', 'commercial-projects.html')

# 2. Create new scripts for new categories
def create_new_project_script(new_file, new_html, h2_text, images):
    template = f"""
with open('index.html', 'r', encoding='utf-8') as f:
    template = f.read()

start_marker = '<div id="main-content">'
end_marker = '<footer class="et-l et-l--footer">'
start_idx = template.find(start_marker)
end_idx = template.find(end_marker)
header_html = template[:start_idx + len(start_marker)]
footer_html = template[template.rfind('</div>', 0, end_idx) : ]

css = '''
<style>
.outdoor-page {{ font-family: Open Sans, Arial, sans-serif; color: #333; background-color: #fff; padding-bottom: 80px; }}
.outdoor-hero {{ background-color: #eef3fc; padding: 60px 20px; }}
.outdoor-hero-content {{ max-width: 1080px; margin: 0 auto; display: flex; justify-content: space-between; align-items: center; gap: 40px; }}
.outdoor-hero-text h2 {{ color: #333; font-size: 26px; font-weight: bold; margin: 0 0 15px 0; }}
.outdoor-hero-text p {{ color: #555; font-size: 15px; margin: 0; }}
.outdoor-btn {{ display: inline-block; background-color: #142ea7; color: #fff !important; padding: 15px 30px; border-radius: 5px; font-weight: bold; text-decoration: none; }}
.outdoor-btn:hover {{ background-color: #006edd; }}
.outdoor-gallery {{ max-width: 1080px; margin: 60px auto 0; padding: 0 20px; display: grid; grid-template-columns: repeat(3, 1fr); gap: 20px; }}
.outdoor-gallery img {{ width: 100%; height: auto; border-radius: 5px; }}
</style>
'''

images_html = ""
for img in {images}:
    images_html += f'<div class="gallery-item"><img src="{{img}}" alt="Project Image" /></div>'

html_out = f'''
<div class="outdoor-page">
    <div class="outdoor-hero">
        <div class="outdoor-hero-content">
            <div class="outdoor-hero-text">
                <h2>{h2_text}</h2>
                <p>Check out our recent projects in this category.</p>
            </div>
            <a href="/contact.html" class="outdoor-btn">Contact Us</a>
        </div>
    </div>
    <div class="outdoor-gallery">
        {{images_html}}
    </div>
</div>
'''

head_end_idx = header_html.find('</head>')
header_html = header_html[:head_end_idx] + css + header_html[head_end_idx:]

final_html = header_html + html_out + footer_html

with open('{new_html}', 'w', encoding='utf-8') as f:
    f.write(final_html)
print("Generated {new_html}")
"""
    with open(new_file, 'w') as f:
        f.write(template)

create_new_project_script('build_step_projects.py', 'step-projects.html', 'Step Projects', ['"https://pageconcretenc.com/wp-content/uploads/2024/11/564bf375-4896-43b9-bd69-1f4127d72055.jpg"'])
create_new_project_script('build_fencing_projects.py', 'fencing-projects.html', 'Fencing Projects', ['"https://pageconcretenc.com/wp-content/uploads/2024/11/c22f1afe-1892-4ed3-934a-865c4932add1.jpg"'])
create_new_project_script('build_deck_projects.py', 'deck-projects.html', 'Deck Projects', ['"https://pageconcretenc.com/wp-content/uploads/2024/11/2d0f4cc6-f757-48bd-8851-b8fb4759c287-scaled.jpg"'])
create_new_project_script('build_outdoor_structure_projects.py', 'outdoor-structure-projects.html', 'Outdoor Structure Projects', ['"https://pageconcretenc.com/wp-content/uploads/2024/01/NAC-Inc-Meadowlands-Community-Park-Improvement-3.jpeg"', '"https://pageconcretenc.com/wp-content/uploads/2024/11/e2c568f4-ec63-490d-a04d-f39ab0f0aa6c.jpg"'])

print("Migration script generated all project build files.")

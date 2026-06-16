with open('service-area.html', 'r', encoding='utf-8') as f:
    lines = f.readlines()

map_start = -1
map_end = -1
seo_start = -1
seo_end = -1

for i, line in enumerate(lines):
    if '<div class="service-section map-section">' in line:
        map_start = i
    if '<div class="service-section seo-content">' in line:
        seo_start = i
    if '<!-- Sticky Call Button -->' in line:
        seo_end = i - 1  # The div closes on the line before the sticky button

if map_start != -1 and seo_start != -1:
    map_end = seo_start - 1
    
    # Extract map section
    map_section_lines = lines[map_start:map_end]
    
    # Extract before map
    before_map = lines[:map_start]
    
    # Extract seo content
    seo_content_lines = lines[seo_start:seo_end+1]
    
    # Extract after seo content
    after_seo = lines[seo_end+1:]
    
    # Reassemble
    new_lines = before_map + seo_content_lines + ['\n'] + map_section_lines + after_seo
    
    with open('service-area.html', 'w', encoding='utf-8') as f:
        f.writelines(new_lines)
    print("Successfully moved map section")
else:
    print(f"Failed to find sections. map_start={map_start}, seo_start={seo_start}")


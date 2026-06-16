import os
import re

files = ['index.html', 'patios.html', 'driveways.html', 'sidewalks.html', 'stamped-concrete.html']

new_fix = """
    <style>
        /* Bulletproof Gap Fix */
        body #page-container {
            padding-top: 0 !important;
            margin-top: 0 !important;
        }
        body #top-header {
            position: relative !important;
        }
        body #main-header {
            position: sticky !important;
            top: 0 !important;
            z-index: 999999 !important;
            box-shadow: 0 2px 10px rgba(0,0,0,0.1) !important;
        }
        body #et-main-area {
            margin-top: 0 !important;
            padding-top: 0 !important;
        }
        body #main-content, 
        body #main-content .service-page-container,
        body .et_builder_inner_content {
            margin-top: 0 !important;
            padding-top: 0 !important;
        }
        body .et_pb_section_0, 
        body .service-hero {
            margin-top: 0 !important;
        }
    </style>
</head>
"""

for file in files:
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()

    # Remove the old fix block if it exists
    content = re.sub(r'<style>\s*/\* Remove any gap between header and hero section \*/.*?</script>', '', content, flags=re.DOTALL)
    
    # Remove any leftover bulletproof fix just in case
    content = re.sub(r'<style>\s*/\* Bulletproof Gap Fix \*/.*?</style>', '', content, flags=re.DOTALL)

    # Inject the new bulletproof fix
    content = content.replace('</head>', new_fix)

    with open(file, 'w', encoding='utf-8') as f:
        f.write(content)

print("Bulletproof gap fix applied.")

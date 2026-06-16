import os

files = ['index.html', 'patios.html', 'driveways.html', 'sidewalks.html', 'stamped-concrete.html']

fix_code = """
    <style>
        /* Remove any gap between header and hero section */
        #main-content, 
        #main-content article, 
        #main-content .entry-content, 
        #main-content .et-boc, 
        #main-content .et-l, 
        #main-content .et_builder_inner_content, 
        .service-page-container {
            padding-top: 0 !important;
            margin-top: 0 !important;
        }
        .et_pb_section_0, .service-hero {
            margin-top: 0 !important;
        }
    </style>
    <script>
        document.addEventListener("DOMContentLoaded", function() {
            function adjustGap() {
                var header = document.getElementById('main-header');
                var topHeader = document.getElementById('top-header');
                var pageContainer = document.getElementById('page-container');
                
                if (header && pageContainer) {
                    var headerHeight = header.offsetHeight;
                    if (topHeader && window.getComputedStyle(topHeader).display !== 'none') {
                        headerHeight += topHeader.offsetHeight;
                    }
                    pageContainer.style.setProperty('padding-top', headerHeight + 'px', 'important');
                }
            }
            adjustGap();
            setTimeout(adjustGap, 500); // Catch any late layout shifts
            window.addEventListener('load', adjustGap);
            window.addEventListener('resize', adjustGap);
        });
    </script>
</head>
"""

for file in files:
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()

    if "/* Remove any gap between header and hero section */" not in content:
        content = content.replace('</head>', fix_code)

        with open(file, 'w', encoding='utf-8') as f:
            f.write(content)

print("Gap fix applied.")

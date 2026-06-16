import re

files = ['index.html', 'patios.html', 'driveways.html', 'sidewalks.html', 'stamped-concrete.html']

nuclear_script = """
    <script>
        // Nuclear option to prevent Divi from adding phantom padding
        document.addEventListener('DOMContentLoaded', function() {
            document.body.classList.remove('et_fixed_nav');
            document.body.classList.add('et_non_fixed_nav');
            
            var pc = document.getElementById('page-container');
            if (pc) {
                // Forcefully remove inline padding applied by Divi JS
                var killPadding = setInterval(function() {
                    if (pc.style.paddingTop) {
                        pc.style.removeProperty('padding-top');
                    }
                    if (pc.style.marginTop) {
                        pc.style.removeProperty('margin-top');
                    }
                }, 50);
                
                // Stop the interval after a few seconds once Divi is done loading
                setTimeout(function() { clearInterval(killPadding); }, 3000);
            }
        });
    </script>
</head>
"""

for file in files:
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()

    # Replace class in body tag
    content = content.replace('et_fixed_nav', 'et_non_fixed_nav')

    # Inject the nuclear script
    if "Nuclear option to prevent Divi" not in content:
        content = content.replace('</head>', nuclear_script)

    with open(file, 'w', encoding='utf-8') as f:
        f.write(content)

print("Nuclear gap fix applied.")

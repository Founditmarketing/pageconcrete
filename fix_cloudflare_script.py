import re
import glob

files = glob.glob('*.html')

for file in files:
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()

    # Remove the bad script tag
    content = re.sub(r'<script[^>]*src="/cdn-cgi/[^>]*></script>', '', content)
    
    with open(file, 'w', encoding='utf-8') as f:
        f.write(content)

print("Removed Cloudflare scripts")

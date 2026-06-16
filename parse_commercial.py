import re
from bs4 import BeautifulSoup

with open('live_commercial.html', 'r', encoding='utf-8') as f:
    html = f.read()

soup = BeautifulSoup(html, 'html.parser')

print("Parsed sections:")
# The live site might have h2s for the titles
headings = soup.find_all('h2')
for h in headings:
    print(h.text.strip())

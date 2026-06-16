import os
from bs4 import BeautifulSoup

cities = [
    "High Point",
    "Greensboro",
    "Winston-Salem",
    "Kernersville",
    "Thomasville",
    "Oak Ridge",
    "Summerfield",
    "Clemmons",
    "Lexington",
    "Colfax",
    "Archdale",
    "Jamestown",
    "Walkertown",
    "Walburg",
    "Trinity",
    "Union Cross",
    "Midway"
]

with open('service-area.html', 'r', encoding='utf-8') as f:
    base_html = f.read()

for city in cities:
    slug = city.lower().replace(' ', '-').replace(',', '')
    filename = f"{slug}.html"
    
    # Simple string replacements to customize the page for the city
    html = base_html
    
    # Meta tags
    html = html.replace('<title>Concrete Contractor Services In High Point Greensboro Winston Salem</title>', f'<title>Concrete Contractor Services in {city}, NC</title>')
    html = html.replace('content="Concrete Contractor Services for Residential And Commercial In High Point, Greensboro, Kernersville, Clemmons, Winston-salem, NC. Concrete Patios, Driveways, Sidewalks"', f'content="Concrete Contractor Services for Residential and Commercial in {city}, NC. Concrete Patios, Driveways, Sidewalks"')
    html = html.replace('content="Concrete Contractor Services In High Point Greensboro Winston Salem"', f'content="Concrete Contractor Services in {city}, NC"')
    
    # Hero Title
    html = html.replace('<h1>Service Area</h1>', f'<h1>Concrete Contractor Services in {city}, NC</h1>')
    
    # Map Section Title
    html = html.replace('<h2>Located in High Point NC, and service in the surrounding areas.</h2>', f'<h2>Serving {city}, NC and surrounding areas.</h2>')
    
    # Locations Grid text
    html = html.replace('Serving the Triad and Surrounding Areas', f'Serving {city} and the Triad')
    
    # SEO Text replacements (making it specific to the city)
    html = html.replace('High Point, Greensboro, Kernersville, Clemmons, Winston-salem', city)
    html = html.replace('the Triad', city)
    
    # Ensure active menu is still Service Area
    # (Already handled since we cloned from service-area.html)
    
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(html)
    
    print(f"Generated {filename}")

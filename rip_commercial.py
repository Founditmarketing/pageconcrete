import requests

url = "https://pageconcretenc.com/commercial/"
headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7)'
}
response = requests.get(url, headers=headers)
html = response.text

with open('live_commercial.html', 'w', encoding='utf-8') as f:
    f.write(html)
print(f"Downloaded {len(html)} bytes")

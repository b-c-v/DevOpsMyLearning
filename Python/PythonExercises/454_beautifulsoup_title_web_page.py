from bs4 import BeautifulSoup
import requests

# python3 -m venv .tmp
# source .tmp/bin/activate
# pip install requests beautifulsoup4

url = "https://weldering.com"
req = requests.get(url, timeout=3)
text = BeautifulSoup(req.text, "html.parser")
site_title = text.title.string
print(site_title)
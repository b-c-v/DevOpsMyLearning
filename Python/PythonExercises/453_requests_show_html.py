import requests

# python3 -m venv .tmp
# source .tmp/bin/activate
# pip install requests

site = "https://weldering.com"
page = requests.get(url=site)
page_html = page.text
print(page_html)
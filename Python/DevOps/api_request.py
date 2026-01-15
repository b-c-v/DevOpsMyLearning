import requests  # Library for working with API requests

# python3 -m venv .tmp
# source .tmp/bin/activate
# pip install requests

username = "francoisrose"

response = requests.get(f"https://gitlab.com/api/v4/users/{username}/projects")
response_json = response.json()

print(response_json)
for project in response_json:
    print(f"Project name: {project['name']}\nProject URL: {project['web_url']}")

import requests

GITLAB_URL = "https://gitlab.com/api/v4/projects"
TOKEN = "YOUR_PAT"

headers = {
    "PRIVATE-TOKEN": TOKEN
}

response = requests.get(GITLAB_URL, headers=headers)

print("Status Code:", response.status_code)

for project in response.json():
    print(project["name"])

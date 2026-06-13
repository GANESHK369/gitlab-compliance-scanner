import requests

TOKEN = "your_pat"

response = requests.get(
    "https://gitlab.com/api/v4/projects?owned=true",
    headers={"PRIVATE-TOKEN": TOKEN}
)

print("Status:", response.status_code)

for project in response.json():
    print(project["name"])

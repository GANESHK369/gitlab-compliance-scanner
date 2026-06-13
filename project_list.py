import requests

GITLAB_URL = "https://gitlab.com/api/v4/projects"
TOKEN = "glpat-x1BtidXZPp3pF8WIP4MzLWM6MQpvOjEKdTpqNGtyeQ8.01.170yjxg6o"

headers = {
    "PRIVATE-TOKEN": TOKEN
}

response = requests.get(GITLAB_URL, headers=headers)

print("Status Code:", response.status_code)

for project in response.json():
    print(project["name"])

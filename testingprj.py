import requests

TOKEN = "glpat-x1BtidXZPp3pF8WIP4MzLWM6MQpvOjEKdTpqNGtyeQ8.01.170yjxg6o"

response = requests.get(
    "https://gitlab.com/api/v4/projects?owned=true",
    headers={"PRIVATE-TOKEN": TOKEN}
)

print("Status:", response.status_code)

for project in response.json():
    print(project["name"])

import requests
from config import GITLAB_URL, HEADERS

def check_webhook(project_id):

    url = f"{GITLAB_URL}/projects/{project_id}/hooks"

    response = requests.get(url, headers=HEADERS)

    if response.status_code != 200:
        return "ERROR"

    hooks = response.json()

    if len(hooks) > 0:
        return "PASS"

    return "FAIL"

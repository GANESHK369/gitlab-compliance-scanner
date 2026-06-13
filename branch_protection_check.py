import requests
from config import GITLAB_URL, HEADERS

def check_branch_protection(project_id):

    url = f"{GITLAB_URL}/projects/{project_id}/protected_branches"

    response = requests.get(url, headers=HEADERS)

    if response.status_code != 200:
        return "ERROR"

    branches = response.json()

    if len(branches) > 0:
        return "PASS"

    return "FAIL"

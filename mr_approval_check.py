import requests
from config import GITLAB_URL, HEADERS

def check_mr_approval(project_id):

    url = f"{GITLAB_URL}/projects/{project_id}/approvals"

    response = requests.get(url, headers=HEADERS)

    if response.status_code != 200:
        return "ERROR"

    approval = response.json()

    required = approval.get("approvals_required", 0)

    if required > 0:
        return "PASS"

    return "FAIL"

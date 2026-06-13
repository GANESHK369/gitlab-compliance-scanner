import requests

from config import GITLAB_URL, HEADERS

from branch_protection_check import check_branch_protection
from webhook_check import check_webhook
from mr_approval_check import check_mr_approval


def get_projects():

    url = f"{GITLAB_URL}/projects?owned=true&membership=true&visibility=private"

    response = requests.get(url, headers=HEADERS)

    print("Status Code:", response.status_code)

    try:
        data = response.json()
    except Exception as e:
        print("Failed to parse JSON:", e)
        return []

    print(f"Projects Found: {len(data)}")
    
    for project in data:
        print(project["name"])

    if not isinstance(data, list):
        print("ERROR: Expected a list of projects.")
        return []

    return data


def main():

    projects = get_projects()

    if not projects:
        print("No projects found or API returned an error.")
        return

    print(
        f"{'Repository':25}"
        f"{'Branch Protection':20}"
        f"{'Webhook':12}"
        f"{'MR Approval':12}"
    )

    print("-" * 75)

    for project in projects:

        project_id = project.get("id")
        project_name = project.get("name", "UNKNOWN")

        bp = check_branch_protection(project_id)

        wh = check_webhook(project_id)

        mr = check_mr_approval(project_id)

        print(
            f"{project_name:25}"
            f"{bp:20}"
            f"{wh:12}"
            f"{mr:12}"
        )


if __name__ == "__main__":
    main()

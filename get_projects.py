def get_projects():

    url = f"{GITLAB_URL}/projects?owned=true"

    response = requests.get(url, headers=HEADERS)

    print("Status Code:", response.status_code)
    print("Response:", response.json())

    return response.json()

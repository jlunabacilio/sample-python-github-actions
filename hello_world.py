import requests
from requests.auth import HTTPBasicAuth
import json
import os

def helloWorld(url, JIRA_USR, JIRA_API_TKN):
    auth = HTTPBasicAuth(JIRA_USR, JIRA_API_TKN)

    headers = {
        "Accept": "application/json"
    }

    response = requests.request(
        "GET",
        url,
        headers=headers,
        auth=auth
    )

    issue = response.status_code
    print(issue)
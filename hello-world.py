import requests
from requests.auth import HTTPBasicAuth
import json
import os

JIRA_USR = os.environ["CI_JIRA_USR"]
JIRA_API_TKN = os.environ["CI_JIRA_API_TKN"]

url = "https://aeromexico.atlassian.net/rest/api/3/issue/"+ "PERS0-64"

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
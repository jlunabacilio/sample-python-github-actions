from hello_world import *

JIRA_USR = os.getenv("JIRA_USR")
JIRA_API_TKN = os.getenv("JIRA_API_TKN")

url = "https://aeromexico.atlassian.net/rest/api/3/issue/"+ "PERS0-64"

helloWorld(url, JIRA_USR, JIRA_API_TKN)
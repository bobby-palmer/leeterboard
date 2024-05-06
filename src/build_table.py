import requests
import json

BASE_URL = "https://leetcode-stats-api.herokuapp.com/"
USERLIST = "bin/users.json"

with open(USERLIST, 'r') as u:
    global users
    users = json.load(u)

rankings = []

for username, user in users.items():
    res = requests.get(BASE_URL + username).json()
    score = res["easySolved"] + 2 * res["mediumSolved"] + 3 * res["hardSolved"]
    rankings.append((score, user))

rankings.sort()
rankings.reverse()

# make table
with open("readme.md", 'w') as f:
    f.write("# Leeterboard\n")
    f.write("an automatic leaderboard for leetcode stats\n")
    f.write("## How to join\n")
    f.write('Open a new issue with the title : `<leetcode username> <first name> <last name>`  \n')
    f.write('For example, I would open a new issue titled : bobbypalmer Bobby Palmer  \n')
    f.write("## Scoring\n")
    f.write("You score is calculated as : 3 * hards solved + 2 * mediums solved + 1 * easys solved  \n")
    f.write("## Leaderboard\n")
    f.write("| Name | Score |\n")
    f.write("| --- | --- |\n")
    for score, user in rankings:
        f.write(f"| {user} | {score} |\n")


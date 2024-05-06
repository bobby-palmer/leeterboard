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
    f.write("| Name | Score |\n")
    f.write("| --- | --- |\n")
    for score, user in rankings:
        f.write(f"| {user} | {score} |\n")


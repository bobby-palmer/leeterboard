import json

import requests

BASE_URL = "https://leetcode-stats-api.herokuapp.com/"
USERLIST = "bin/users.json"

with open(USERLIST, "r") as u:
    global users
    users = json.load(u)

rankings = []

for username, user in users.items():
    res = requests.get(BASE_URL + username).json()
    while res['status'] != 'success':
        res = requests.get(BASE_URL + username).json()

    score = res["easySolved"] + 2 * res["mediumSolved"] + 3 * res["hardSolved"]
    rankings.append(
        (
            score,
            user,
            res["easySolved"],
            res["mediumSolved"],
            res["hardSolved"],
        )
    )

rankings.sort()
rankings.reverse()

with open("readme.md", "r") as f:
    lines = f.readlines()

# make table
with open("readme.md", "w") as f:
    for line in lines:
        f.write(line)
        if line.strip() == "## Leaderboard":
            break
    f.write("| Name | Easy | Medium | Hard | Score |\n")
    f.write("| --- | --- | --- | --- | --- |\n")
    for score, user, easy, medium, hard in rankings:
        f.write(f"| {user} | {easy} | {medium} | {hard} | {score} |\n")

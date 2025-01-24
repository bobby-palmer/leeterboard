import json

import requests

BASE_URL = "https://alfa-leetcode-api.onrender.com/"
USERLIST = "bin/users.json"

with open(USERLIST, "r") as u:
    global users
    users = json.load(u)

rankings = []

for username, user in users.items():
    print("getting " + username)
    res = requests.get(BASE_URL + username + "/solved")

    while res.status_code != 200:
        res = requests.get(BASE_URL + username + "/solved")

    res = res.json()

    score = res["easySolved"] + 3 * res["mediumSolved"] + 6 * res["hardSolved"]
    rankings.append(
        (
            score,
            user[0],
            res["easySolved"],
            res["mediumSolved"],
            res["hardSolved"],
            score - user[1],
        )
    )

    # store the last score to calculate updates
    users[username][1] = score

with open(USERLIST, "w") as f:
    f.write(json.dumps(users))

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
    f.write("| Name | Easy | Medium | Hard | Score | 1 Day Change |\n")
    f.write("| --- | --- | --- | --- | --- | --- |\n")
    for score, user, easy, medium, hard, change in rankings:
        change_str = "-"
        if change > 0:
            change_str = f"$\\color{{green}}{{+{change}}}$"
        f.write(f"| {user} | {easy} | {medium} | {hard} | {score} | {change_str} |\n")

import json
import sys

import requests

BASE_URL = "https://alfa-leetcode-api.onrender.com/"
USERLIST = "bin/users.json"

with open(USERLIST, "r") as u:
    global users
    users = json.load(u)

if len(sys.argv) != 4:
    exit(0)

username = sys.argv[1]
firstname = sys.argv[2]
lastname = sys.argv[3]

if username in users.keys():
    exit(0)

res = requests.get(BASE_URL + username).json()

if "errors" in res:
    exit(0)

users[username] = (f"{firstname} {lastname}", 0)

with open(USERLIST, "w") as output:
    output.write(json.dumps(users))

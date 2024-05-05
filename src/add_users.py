import requests
import json
import sys

BASE_URL = "https://leetcode-stats-api.herokuapp.com/"
USERLIST = "bin/users.json"

with open(USERLIST, 'r') as u:
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

if res['status'] != 'success':
    exit(0)

users[username] = f"{firstname} {lastname}"

with open(USERLIST, 'w') as output:
    output.write(json.dumps(users))

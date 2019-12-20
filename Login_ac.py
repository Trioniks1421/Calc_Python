import os
import json

file = os.path.join('users.json')


def valid_user_in_db(**check_user):
    with open(file, 'r') as users:
        list_users = json.load(users)
        for user in list_users:
            if user['login'] == check_user["login"] and user['password'] == check_user["password"]:
                return True

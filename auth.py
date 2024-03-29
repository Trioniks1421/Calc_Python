import os
import json



def check_pass(pass1, pass2):
    upper_chr = 0
    digit_pass = 0
    for i in pass1:
        if i.isupper():
            upper_chr += 1
        if i.isdigit():
            digit_pass += 1
    if pass1 == pass2 and len(pass1) >= 8 and upper_chr >= 1 and digit_pass >= 1:
        return True


def register():
    repeat_register = True
    user = None
    while repeat_register:
        login = input('login >>> ')
        password = input('password >>> ')
        confirm_password = input('repeat password >>>')
        if check_pass(password, confirm_password):
            try:
                user = write_to_db(login=login, password=password)
                repeat_register = False
                print('register success!')
            except ValueError as e:
                repeat_register = True
                print(e)
        else:
            print('incorrect password')
    return user


def write_to_db(**new_user):
    file = os.path.join('users.json')

    def check_user_in_db(login):
        #nonlocal file              ###Ошибка
        with open(file, 'r') as users:
            list_users = json.load(users)
            for user in list_users:
                if user['login'] == login:
                    raise ValueError('user already exists with login {}'.format(login))

    with open(file, 'r') as users:
        user_data = json.load(users)
        if len(user_data) == 0:
            new_user.update(
                {'id': 1}
            )
        else:
            check_user_in_db(login=new_user['login'])
            new_id = user_data[-1]['id'] + 1
            new_user.update({
                'id': new_id
            })
    user_data.append(new_user)
    with open(file, 'w+') as f:
        json.dump(user_data, f)
    return new_user


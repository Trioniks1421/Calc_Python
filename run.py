from auth import register
from Login_ac import valid_user_in_db
from Calculator1 import Guest_calc, Auth_calc
import json
import os

print("Please , login or register for the full functionality of the calculator\nLogin or register press (y)\n"
      "Login as guest press (n)")
guest_bool = False
in_elem = (input())
try:
    if in_elem == "y":
        auth_bool = input("Do you have an account? y/n\n")
        if auth_bool == "y":
            loop = True
            while loop:
                try:
                    print("Enter account information")
                    login = input("login=")
                    password = input("password=")
                    if valid_user_in_db(login=login, password=password):
                        loop = False
                        guest_bool = True
                        print("Welcome {}".format(login))
                    else:
                        raise ValueError("Login and password are not entered correctly")
                except ValueError as e:
                    loop = True
                    print(e)
        elif auth_bool == "n":
            print("Enter the data for registration")
            new_user = register()
            if new_user:
                guest_bool = True
            print(new_user)


    elif in_elem == "n" and guest_bool == False:
        Guest_calc()
    else:
        raise ValueError("y OR n !!!!")
    if guest_bool == True:
        Auth_calc()
except ValueError as a:
    print(a)
read_bool = input("View transaction history (y/n)")
file = os.path.join('operation.json')
if read_bool == "y":
    with open(file, "r") as f:
        read_data_operations = json.load(f)
else:
    pass

import json
import os
import sys

# instantiate file with a empty list if file is empty
file_size = os.path.getsize("UserPass.json")
if file_size <= 1:
    with open("UserPass.json", mode='w', encoding='utf-8') as file:
        json.dump([], file)


def check_existing_user(name):
    """loads json file which stores username and password combinations
    and compares the current username to previously saved usernames"""
    with open("UserPass.json") as f:
        list_of_user = json.load(f)
        for users in list_of_user:
            cname = users.pop('username')
            if cname == name:
                return True
    return False


def check_password(u_name, p_word):
    """loads the json file and compares the entered username and password
    combination with the saved ones"""
    with open('UserPass.json', 'r') as f:
        list_of_users = json.load(f)
        for users in list_of_users:
            cname = users.pop('username')
            if cname == u_name:
                cpass = users.pop('password')
                if cpass == p_word:
                    return True
                else:
                    return False


def write_user(u_name, p_word):
    """opens the json file and stores the values into a list of usernames and passwords,
    then appends the new user's information to the list and dumps the updated list back
    into the file"""
    with open('UserPass.json', 'r') as f:
        new_user = {'username': u_name, 'password': p_word}
        list_of_users = json.load(f)
        list_of_users.append(new_user)
    with open('UserPass.json', 'w') as f:
        json.dump(list_of_users, f)


def create_new_user():
    """Creates a new user and validates"""
    new_username = str(input("Please enter a user name: "))
    while check_existing_user(new_username):
        print("That username already exists, please try another")
        new_username = str(input("Please enter a user name: "))

    # username doesnt exist, continue with creating a new user
    new_password = str(input("Please enter a password: "))
    temp_password = str(input("Please confirm your password: "))
    while new_password != temp_password:
        print("Passwords did not match please try again")
        temp_password = str(input("Please confirm your password: "))

    if new_password == temp_password:
        print("Creating new user....")
        write_user(new_username, new_password)


def existing_user():
    """Saved users can login"""
    username = str(input("Please enter your username: "))
    while not check_existing_user(username):
        print("Sorry, your username was not found")
        username = str(input("Please enter your username again: "))

    password = str(input("Please enter your password: "))
    counter = 0
    while not (check_password(username, password)):
        counter += 1
        if counter >= 3:
            print("Invalid amount of tries. Exiting...\n")
            os._exit(1)
        print("Sorry, your password is incorrect\nYou have " + str(3 - counter) + " tries left")
        password = str(input("Please enter your password again: "))

    # successful login performed
    print("\nWelcome " + username + "!")


"""Program begins"""
choice = ""
while choice != "exit":
    choice = str(input("Would you like to login, create an account, or exit? (Login/Create/Exit)\n")).lower()
    if choice == "create":
        create_new_user()
    elif choice == "login":
        existing_user()
        sys.exit()
    else:
        print("Invalid command. Please try again.")

sys.exit()

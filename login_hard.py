import csv

open_file = open("info_hard.csv")
info = open_file.readlines()
open_file.close

def login():
    with open("info_hard.csv") as open_file:
        contents = list(csv.DictReader(open_file))

    done = False
    while done == False:
        user_name = input("Enter your username: \n>")
        password = input("Enter your password: \n>")
        for row in contents:
            username_place = row['Username']
            password_place = row['Password']
            if user_name == username_place and password == password_place:
                    print("Welcome Back {}".format(row['Full Name']))
                    done = True
            else:
                continue


def user_choice():
    if choice == "c":
        user_name= input("Enter a new username:\n>")
        with open("info.csv") as open_file:
            contents = csv.DictReader(open_file)
            for row in contents:
                username_place = row['Username']
                while user_name == username_place:
                    user_name = input("Username already Exists. Try another Username.\n>")

        password = input("What is your password?\n>")
        full_name = input("What is your full name?\n>")
        fact = input("What is a fun fact about you?\n>")

        with open("info.csv", "a") as open_file:

            fieldnames= ["Username", "Password", "Full Name", "Fact"]
            add_contents = csv.DictWriter(open_file, fieldnames = fieldnames)

            add_contents.writerow({"Username": "{}".format(user_name),"Password": "{}".format(password),
                             "Full Name": "{}".format(full_name), "Fact": "{}".format(fact)})

    if choice == "u":
        user_name = input("Enter the username you wish to update information:\n>")
        with open("info_hard.csv", "a") as open_file:
            fieldnames = ["Username", "Password", "Full Name", "Fact"]
            new_contents = csv.DictWriter(open_file, fieldnames = fieldnames)
            for row in new_contents:
                username_place = row['Username']
                new_choice = input("Would you like to update your (p)assword or your (f)act").lower()
                if new_choice == 'p':
                    new_password = input("What is your new password?\n>")
                    add_contents.writerow({"Password": "{}".format(new_password)})


    else:
        print("You have succesfully logged out!")


login()
choice = input("Would you like to (c)reate a new user, (u)pdate an account, or (l)og out?\n>").lower()
user_choice()

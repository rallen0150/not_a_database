import csv

open_file = open("info.csv")
info = open_file.readlines()
open_file.close

def login():
    with open("info.csv") as open_file:
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
                print("Invalid Login. Try Again!")
                continue


def user_choice():
    if choice == "c":
        user_name= input("Enter a new username:\n>")
        with open("info.csv") as open_file:
            contents = csv.DictReader(open_file)
            for row in contents:
                username_place = row['Username']
                if user_name == username_place:
                    user_name = input("Username already Exists. Try another Username.\n>")

        password = input("What is your password?\n>")
        full_name = input("What is your full name?\n>")
        fact = input("What is a fun fact about you?\n>")

        with open("info.csv", "a") as open_file:

            fieldnames= ["Username", "Password", "Full Name", "Fact"]
            add_contents = csv.DictWriter(open_file, fieldnames = fieldnames)

            add_contents.writerow({"Username": "{}".format(user_name),"Password": "{}".format(password),
                             "Full Name": "{}".format(full_name), "Fact": "{}".format(fact)})
    else:
        print("You have succesfully logged out!")


login()
choice = input("Would you like to (c)reate a new user? Or (l)og out?\n>").lower()
user_choice()
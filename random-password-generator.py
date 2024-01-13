import random 
import string

def generate_password(length):
    characters = list(string.ascii_letters + string.digits + "!@#$%^&*()")
    random.shuffle(characters)
    password = []
    for x in range(password_length):
        password.append(random.choice(characters))

    random.shuffle(password)
    password = "".join(password)
    return password

while True:
    yes_or_no = input("Do you want to generate a password? (y/n): ")
    if yes_or_no == "y":
        password_length = int(input("Enter Password length: "))
        password = generate_password(password_length)
        print(f"Your Password is: {password}")
    elif yes_or_no == "n":
        print("Program ended.")
        quit()
    else:
        print("Invalid input, please enter y for yes or n for no!")
        print("")
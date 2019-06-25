import json


def addition(a, b):
    """Adds two numbers if they are both numbers"""

    try:
        result = int(a) + int(b)
    except ValueError:
        # Using ValueError instead of TypeError to catch error when trying to convert text to int
        print("Sorry, at least one input is not a number. Please try again.\n")
    else:
        print(f"The sum is {result}.\n")


def get_favorite_number():
    filename = "favorite_numbers.json"
    prompt = str("What's your favorite number? ")

    try:
        with open(filename) as file_object:
            favorite_number = json.load(file_object)
    except FileNotFoundError:
        with open(filename, "w") as file_object:
            favorite_number = input(prompt)
            json.dump(favorite_number, file_object)
    else:
        print(f"I know your favorite number! It's {favorite_number}.")


def get_stored_username():
    """Get stored username if available."""
    filename = 'username.json'
    try:
        with open(filename) as f_obj:
            username = json.load(f_obj)
    except FileNotFoundError:
        return None
    else:
        return username


def get_new_username():
    """Prompt for a new username."""
    username = input("What is your name? ")
    filename = 'username.json'
    with open(filename, 'w') as f_obj:
        json.dump(username, f_obj)
        return username


def greet_user():
    """Greet the user by name."""
    username = get_stored_username()

    correct_username_answer = input(f"Is {username} the correct username? (y/n) ")

    if correct_username_answer == 'y':
        print("Welcome back, " + username + "!")
    elif correct_username_answer == 'n':
        username = get_new_username()
        print("We'll remember you when you come back, " + username + "!")
    else:
        print("Sorry, didn't get a y/n response. Try again.")
        greet_user()


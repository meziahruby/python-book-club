class Restaurant():
    """A simple restaurant"""

    def __init__(self, restaurant_name, cuisine_type, number_served=0):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = number_served

    def desecribe_restaurant(self):
        print(f"{self.restaurant_name} has {self.cuisine_type} cuisine.")

    def open_restaurant(self):
        print(f"{self.restaurant_name} is open!")

    def set_number_served(self, number_served):
        self.number_served = number_served

    def increment_number_served(self, increment_number):
        if increment_number < 0:
            print("You can't increment the number of customers by a negative number!")
        else:
            self.number_served += increment_number


class User():
    """A simple user"""

    def __init__(self, first_name, last_name, age, sex, login_attempts=0):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.sex = sex
        self.login_attempts = login_attempts

    def describe_user(self):
        if self.sex.lower() == "male":
            pronoun = "He"
        elif self.sex.lower() == "female":
            pronoun = "She"
        else:
            pronoun = "He/she"

        print(f"This user's name is {self.first_name} {self.last_name}. {pronoun} is {self.age} year(s) old.")

    def greet_user(self):
        print(f"Hi, {self.first_name}! It's nice to meet you!")

    def increment_login_attempts(self):
        self.login_attempts +=1

    def reset_login_attempts(self):
        self.login_attempts = 0



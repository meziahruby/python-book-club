from random import randint


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


class IceCreamStand(Restaurant):
    """A simple ice cream stand"""

    def __init__(self, restaurant_name, cuisine_type, flavors, number_served=0):
        super().__init__(restaurant_name, cuisine_type, number_served)
        self.flavors = flavors

    def show_flavors(self):
        print("These are the ice cream stand's available flavors:")
        for flavor in self.flavors:
            print(f"-{flavor}")


class User():
    """A simple user"""

    def __init__(self, first_name, last_name, age, sex):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.sex = sex
        self.login_attempts = 0

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


class Privileges():
    """A list of privileges"""

    def __init__(self, privileges=[]):
        self.privileges = privileges

    def show_privileges(self):
        print("These are the privileges:")
        for privilege in self.privileges:
            print(f"-{privilege}")


class Admin(User):
    """A special user, or admin, that has extra privileges"""

    def __init__(self, first_name, last_name, age, sex, user_privileges):
        super().__init__(first_name, last_name, age, sex)
        self.user_privileges = Privileges(user_privileges)
        
        # For 9-7
        # self.privileges = privileges

    # For 9-7
    # def show_privileges(self):
    #     print("These are the admin's privileges:")
    #     for privilege in self.privileges:
    #         print(f"-{privilege}")


class Die():
    """A number-sided die, with default of 6 sides"""

    def __init__(self, sides=6):
        self.sides = sides

    def roll_die(self):
        return randint(1, self.sides)

    def roll_10_times(self):
        for number_of_rolls in range(0, 10):
            print(self.roll_die())


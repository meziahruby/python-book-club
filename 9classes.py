#9-1. Restaurant: Make a class called Restaurant. The __init__() method for
#Restaurant should store two attributes: a restaurant_name and a cuisine_type.
#Make a method called describe_restaurant() that prints these two pieces of
#information, and a method called open_restaurant() that prints a message indicating
#that the restaurant is open.
#Make an instance called restaurant from your class. Print the two attributes
#individually, and then call both methods.
class Restaurant(object):
	def __init__(self, restaurant_name, cuisine_type):
		self.restaurant_name = restaurant_name
		self.cuisine_type = cuisine_type

	def describe_restaurant(self):
		print('This is ' + self.restaurant_name + " and " + self.cuisine_type + '!')

	def open_restaurant(self):
		print('Resturant ' + self.restaurant_name + ' is now open!')

restaurant = Restaurant('Bonjour', 'French')
print(restaurant.restaurant_name + ' and ' + restaurant.cuisine_type)
restaurant.describe_restaurant()
restaurant.open_restaurant()

#9-2. Three Restaurants: Start with your class from Exercise 9-1. Create three
#different instances from the class, and call describe_restaurant() for each
#instance.
restaurant_g = Restaurant('Gutentag', 'German')
restaurant_g.describe_restaurant()

restaurant_p = Restaurant('Hola', 'Mexican')
restaurant_p.describe_restaurant()

restaurant_c = Restaurant('Ni hao', 'Chinese')
restaurant_c.describe_restaurant()

#9-3. Users: Make a class called User. Create two attributes called first_name
#and last_name, and then create several other attributes that are typically stored
#in a user profile. Make a method called describe_user() that prints a summary
#of the user’s information. Make another method called greet_user() that prints
#a personalized greeting to the user.
#Create several instances representing different users, and call both methods
#for each user.
class User(object):
	def __init__(self, first_name, last_name, last_login):
		self.first_name = first_name
		self.last_name = last_name
		self.last_login = last_login
	def describe_user(self):
		print(self.first_name, self.last_name, self.last_login)

	def greet_user(self):
		print('Welcome ' + self.first_name + ' ' + self.last_name + '!')

user_bob = User('Bob', 'Bobby', '123')
user_angie = User('Angie', 'Angela', '234')
user_cat = User('Cat', 'Cathy', '345')

user_bob.describe_user()
user_angie.describe_user()
user_cat.describe_user()

user_bob.greet_user()
user_angie.greet_user()
user_cat.greet_user()

#9-4. Number Served: Start with your program from Exercise 9-1 (page 166).
#Add an attribute called number_served with a default value of 0. Create an
#instance called restaurant from this class. Print the number of customers the
#restaurant has served, and then change this value and print it again.
#Add a method called set_number_served() that lets you set the number
#of customers that have been served. Call this method with a new number and
#print the value again.
#Add a method called increment_number_served() that lets you increment
#the number of customers who’ve been served. Call this method with any number
#you like that could represent how many customers were served in, say, a
#day of business.
class Restaurant(object):
	def __init__(self, restaurant_name, cuisine_type):
		self.restaurant_name = restaurant_name
		self.cuisine_type = cuisine_type
		self.number_served = 0

	def describe_restaurant(self):
		print('This is ' + self.restaurant_name + " and " + self.cuisine_type + '!')

	def open_restaurant(self):
		print('Resturant ' + self.restaurant_name + ' is now open!')

	def set_number_served(self, number_served):
		self.number_served = number_served
	def increment_number_served(self):
		self.number_served = self.number_served + 1

restaurant_a = Restaurant('Hello', 'American')
print(restaurant_a.number_served)
restaurant_a.number_served = 10
print(restaurant_a.number_served)

restaurant_a.set_number_served(20)
print(restaurant_a.number_served)

restaurant_a.increment_number_served()
print(restaurant_a.number_served)


#9-5. Login Attempts: Add an attribute called login_attempts to your User
#class from Exercise 9-3 (page 166). Write a method called increment_
#login_attempts() that increments the value of login_attempts by 1. Write
#another method called reset_login_attempts() that resets the value of login_
#attempts to 0.
#Make an instance of the User class and call increment_login_attempts()
#several times. Print the value of login_attempts to make sure it was incremented
#properly, and then call reset_login_attempts(). Print login_attempts again to
#make sure it was reset to 0.
class User(object):
	def __init__(self, first_name, last_name, last_login):
		self.first_name = first_name
		self.last_name = last_name
		self.last_login = last_login
		self.login_attempts = 0
	def describe_user(self):
		print(self.first_name, self.last_name, self.last_login)

	def greet_user(self):
		print('Welcome ' + self.first_name + ' ' + self.last_name + '!')

	def increment_login_attempts(self):
		self.login_attempts = self.login_attempts + 1

	def reset_login_attempts(self):
		self.login_attempts = 0

user_a = User('Amy', 'Ashley', 111)
user_a.increment_login_attempts()
user_a.increment_login_attempts()
user_a.increment_login_attempts()

print(user_a.login_attempts)
user_a.reset_login_attempts()
print(user_a.login_attempts)

#9-6. Ice Cream Stand: An ice cream stand is a specific kind of restaurant. Write
#a class called IceCreamStand that inherits from the Restaurant class you wrote
#in Exercise 9-1 (page 166) or Exercise 9-4 (page 171). Either version of
#the class will work; just pick the one you like better. Add an attribute called
#flavors that stores a list of ice cream flavors. Write a method that displays
#these flavors. Create an instance of IceCreamStand, and call this method.
class IceCreamStand(Restaurant):

	def __init__(self, restaurant_name, cuisine_type, flavors):
		super().__init__(restaurant_name, cuisine_type)
		self.flavors = flavors

	def print_flavors(self):
		print(self.flavors)

ice_cream_a = IceCreamStand('Super Ice', 'ice cream', ['razz', 'apple', 'cheese'])
ice_cream_a.print_flavors()

#9-7. Admin: An administrator is a special kind of user. Write a class called
#Admin that inherits from the User class you wrote in Exercise 9-3 (page 166)
#or Exercise 9-5 (page 171). Add an attribute, privileges, that stores a list
#of strings like "can add post", "can delete post", "can ban user", and so on.
#Write a method called show_privileges() that lists the administrator’s set of
#privileges. Create an instance of Admin, and call your method.
class Admin(User):
	def __init__(self, first_name, last_name, last_login, privileges):
		super().__init__(first_name, last_name, last_login)
		self.privileges = privileges

	def show_privileges(self):
		print(self.privileges)

admin_a = Admin('Joan', 'Arc', '123', ['can add post', 'can ban user', 'can delete post'])
admin_a.show_privileges()


#9-8. Privileges: Write a separate Privileges class. The class should have one
#attribute, privileges, that stores a list of strings as described in Exercise 9-7.
#Move the show_privileges() method to this class. Make a Privileges instance
#as an attribute in the Admin class. Create a new instance of Admin and use your
#method to show its privileges.

class Privleges(object):

	def __init__(self, privleges=['can add post', 'can delete post', 'can ban user']):
		self.privleges = privleges

	def show_privleges(self):
		print(self.privleges)

class User(object):
	def __init__(self, first_name, last_name):
		self.first_name = first_name
		self.last_name = last_name
		self.login_attempts = 0
	def describe_user(self):
		print(self.first_name, self.last_name, self.last_login)

	def greet_user(self):
		print('Welcome ' + self.first_name + ' ' + self.last_name + '!')

	def increment_login_attempts(self):
		self.login_attempts = self.login_attempts + 1

	def reset_login_attempts(self):
		self.login_attempts = 0


class Admin(User):
	def __init__(self, first_name, last_name):
		super().__init__(first_name, last_name)
		self.privleges = Privleges()

admin_jon = Admin('Jon', 'Rain')
admin_jon.privleges.show_privleges()

#9-9. Battery Upgrade: Use the final version of electric_car.py from this section.
#Add a method to the Battery class called upgrade_battery(). This method
#should check the battery size and set the capacity to 85 if it isn’t already.
#Make an electric car with a default battery size, call get_range() once, and
#then call get_range() a second time after upgrading the battery. You should
#see an increase in the car’s range.
class Car(object):
	def __init__(self, make, model, year):
		self.make = make
		self.model = model
		self.year = year
		self.odometer_reading = 0

class Battery(object):
	def __init__(self, battery_size=70):
		self.battery_size = battery_size

	def get_range(self):
		if self.battery_size == 70:
			range = 240
		elif self.battery_size == 85:
			range = 270

		message = 'This car can go approximately ' + str(range)
		message += ' miles on a full charge.'
		print(message)

	def upgrade_battery(self):
		if self.battery_size != 85:
			self.battery_size = 85

class ElectricCar(Car):
	def __init__(self, make, model, year):
		super().__init__(make, model, year)
		self.battery = Battery()

electric_car = ElectricCar('Make A', 'Model A', 'Year 1')
electric_car.battery.get_range()
electric_car.battery.upgrade_battery()
electric_car.battery.get_range()

#9-10. Imported Restaurant: Using your latest Restaurant class, store it in a module.
#Make a separate file that imports Restaurant. Make a Restaurant instance,
#and call one of Restaurant’s methods to show that the import statement is working
#properly.


#9-11. Imported Admin: Start with your work from Exercise 9-8 (page 178).
#Store the classes User, Privileges, and Admin in one module. Create a separate
#file, make an Admin instance, and call show_privileges() to show that
#everything is working correctly.


#9-12. Multiple Modules: Store the User class in one module, and store the
#Privileges and Admin classes in a separate module. In a separate file, create
#an Admin instance and call show_privileges() to show that everything is still
#working correctly.


#9-13. OrderedDict Rewrite: Start with Exercise 6-4 (page 108), where you
#used a standard dictionary to represent a glossary. Rewrite the program using
#the OrderedDict class and make sure the order of the output matches the order
#in which key-value pairs were added to the dictionary.


#9-14. Dice: The module random contains functions that generate random numbers
#in a variety of ways. The function randint() returns an integer in the
#range you provide. The following code returns a number between 1 and 6:
#from random import randint
#x = randint(1, 6)
#Make a class Die with one attribute called sides, which has a default
#value of 6. Write a method called roll_die() that prints a random number
#between 1 and the number of sides the die has. Make a 6-sided die and roll
#it 10 times.
#Make a 10-sided die and a 20-sided die. Roll each die 10 times.
from random import randint

class Die(object):
	def __init__(self, sides=6):
		self.sides = sides
		self.list_rolls = []

	def roll_die(self):
		return randint(1, self.sides)

	def roll_die_many(self, number_rolls):
		#return list of rolls
		for i in range(0, number_rolls):
			self.list_rolls.append(self.roll_die())
		return self.list_rolls

	def print_list_rolls(self):
		print('These are the ' + str(len(self.list_rolls)) + ' rolls for a die with '
		+ str(self.sides) + ' sides:')
		for roll in self.list_rolls:
			print('\t' + str(roll)) 

die_six = Die()
die_six.roll_die_many(10)
die_six.print_list_rolls()

die_ten = Die(10)
die_ten.roll_die_many(10)
die_ten.print_list_rolls()

die_twenty = Die(20)
die_twenty.roll_die_many(10)
die_twenty.print_list_rolls()

#9-15. Python Module of the Week: One excellent resource for exploring the
#Python standard library is a site called Python Module of the Week. Go to
#http://pymotw.com/ and look at the table of contents. Find a module that
#looks interesting to you and read about it, or explore the documentation of
#the collections and random modules.

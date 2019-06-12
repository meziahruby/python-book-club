# sandwich_factory.py
# Extends sandwiches.py and creates a sandwich factory specializing in unique, surprising sandwiches.
# Sandwich orders consist only of customer name and number of ingredients to be used.
# The sandwich machine chooses the are made with random ingredie random recipes book and delivered to franchise locations.

import time
import random

ingredients_list = []

# This defines the steps for the sandwich factory
def sandwich_factory(customer_name, number_of_ingredients):
	print('Got {}\'s order! Constructing your special sandwich...'.format(customer_name))
	generate_recipe(number_of_ingredients)
	assemble_sandwich(customer_name, ingredients_list)
	charge_customer()


# This generates the random sandwich recipe
def generate_recipe(number_of_ingredients):
	# Initialize sandwich options
	filling_options = [
		'lettuce', 'bacon', 'tomato', 'spinach', 'mozarella', 'provolone',
		'cheddar', 'ham', 'olives', 'mayo', 'vinagrette'
		]
	bread_options = [
		'white', 'wheat', 'multigrain', 'jalapeno and cheese', 'brioche'
		]

	# Pick the bread
	print('\t{} was chosen as your bread'.format(random.choice(bread_options)))

	# Pick the fillings
	for i in range(number_of_ingredients):
		random_ingredient = random.choice(filling_options)
		print('\t{} was picked as a random filling'.format(random_ingredient))
		ingredients_list.append(random_ingredient)

	return ingredients_list


# This prints out the sandwich order to the customer
def assemble_sandwich(customer_name, ingredients_list):
	print('\nNow that I have the ingredients, I can make the sandwich. It will take 2 seconds.')
	time.sleep(2)
	print('Okay, I just finished making your random sandwich\n'
		'It has {}. Hope you like it, {}!'.format(ingredients_list, customer_name)
		)

def charge_customer():
	print('You owe ${}. Come again!'.format(random.randint(0,12)))

# Using sandwich_factory
sandwich_factory('Ken', 3)
print('\n...\n')
time.sleep(1)
sandwich_factory('Kevin', 4)
print('\n...\n')
time.sleep(1)
sandwich_factory('Meziah', 5)
print('\n...\n')
time.sleep(1)
sandwich_factory('Michelle', 6)

# 8-12. Sandwiches
# Write a function that accepts a list of items a person wants on a sandwich.
# The function should have one parameter that collects as many items as the function call provides,
# and it should print a summary of the sandwich that is being ordered.
# Call the function three times, using a different number of arguments each time.

import time

def sandwiches(customer_name, *ingredients):

	finished_sandwich = []
	# Greet customer
	print('Hi, {}! I got your sandwich order with: '.format(customer_name))
	for i in range(len(ingredients)):
		# Repeat ingredient to customer
		print('\t ' + ingredients[i])
		# Add each_ingredient to the finished_sandwich
		finished_sandwich.append(ingredients[i])

	# Simulate the fastest sandwich making ever
	print('Please wait 3 seconds while I make it...')
	time.sleep(3)

	# Print summary of sandwich made
	print('Done! Here\'s your {} sandwich. Enjoy!\n'.format(finished_sandwich))

sandwiches('Misha', 'ham', 'eggs', 'brioche buns')
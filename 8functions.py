#8-1. Message: Write a function called display_message() that prints one sentence
#telling everyone what you are learning about in this chapter. Call the
#function, and make sure the message displays correctly.

def display_message():
	print('Message printed')

display_message()
#8-2. Favorite Book: Write a function called favorite_book() that accepts one
#parameter, title. The function should print a message, such as One of my
#favorite books is Alice in Wonderland. Call the function, making sure to
#include a book title as an argument in the function call.

def favorite_book(title):
	print('One of my favorite books is ' + title)

favorite_book('alice in wonderland')


#8-3. T-Shirt: Write a function called make_shirt() that accepts a size and the
#text of a message that should be printed on the shirt. The function should print
#a sentence summarizing the size of the shirt and the message printed on it.
#Call the function once using positional arguments to make a shirt. Call the
#function a second time using keyword arguments.
def make_shirt(size, message):
	print('size of shirt ' + size)
	print('message ' + message)

make_shirt(message = 'poop', size='M')
make_shirt('M', 'poop')
#8-4. Large Shirts: Modify the make_shirt() function so that shirts are large
##by default with a message that reads I love Python. Make a large shirt and a
#m#edium shirt with the default message, and a shirt of any size with a different
#message.
def make_shirt(size='L', message='I love python'):
	print('size of shirt ' + size)
	print('message ' + message)

make_shirt(message = 'poop', size='M')
make_shirt('M', 'poop')
make_shirt()
make_shirt('M')


#8-5. Cities: Write a function called describe_city() that accepts the name of
#a city and its country. The function should print a simple sentence, such as
#Reykjavik is in Iceland. Give the parameter for the country a default value.
#Call your function for three different cities, at least one of which is not in the
#default country.
def describe_city(city, country='Denmark'):
	print(city + ' is in ' + country)

describe_city('baltimore')
describe_city('detroit', 'Netherlands')

#8-6. City Names: Write a function called city_country() that takes in the name
#of a city and its country. The function should return a string formatted like this:
#"Santiago, Chile"
#Call your function with at least three city-country pairs
def city_country(city, country):
	return (city + ", " +country)

print(city_country("Springfield", "Mexico"))

#8-7. Album: Write a function called make_album() that builds a dictionary
#describing a music album. The function should take in an artist name and an
#album title, and it should return a dictionary containing these two pieces of
#information. Use the function to make three dictionaries representing different
#albums. Print each return value to show that the dictionaries are storing the
#album information correctly.
#Add an optional parameter to make_album() that allows you to store the
#number of tracks on an album. If the calling line includes a value for the number
#of tracks, add that value to the albums dictionary. Make at least one new 
#function call that includes the number of tracks on an album.
def make_album(artist, title, tracks=''):
	if tracks :
		return {"artist":artist, 'title':title, 'tracks':tracks}
	else:
		return {"artist":artist, 'title':title}
print(make_album('Bob Dylan', 'Love Yourself'))
print(make_album('Bob Dylan', 'Love Yourself', 12))
##8-8. User Albums: Start with your program from Exercise 8-7. Write a while
#loop that allows users to enter an albums artist and title. Once you have that
#information, call make_album() with the users input and print the dictionary
#thats created. Be sure to include a quit value in the while loop.

print('--------------------8-8\n\n')

message = ''
message2 = ''
while message != 'quit' or message2 != 'quit':
	message = raw_input('enter album artist\n')
	
	if message == 'quit':
		break;
	
	message2 = raw_input('enter album title\n')

	if message2 == 'quit':
		break;
	
	albumDict = (make_album(message, message2))
	print(albumDict)

print('-------------------------thansk')
#8-9. Magicians: Make a list of magicians names. Pass the list to a function
#called show_magicians(), which prints the name of each magician in the list.
magicians = ['y', 'x', 'a']
def show_magicians(magicians):
	for magician in magicians:
		print(magician)

show_magicians(magicians)
#8-10. Great Magicians: Start with a copy of your program from Exercise 8-9.
#Write a function called make_great() that modifies the list of magicians by adding
#the phrase the Great to each magicias name. Call show_magicians() to
#see that the list has actually been modified.
def make_great(magicians):
	for magician in magicians:
		print(magician + ' the Great')

make_great(magicians)
show_magicians(magicians)
#8-11. Unchanged Magicians: Start with your work from Exercise 8-10. Call the
#function make_great() with a copy of the list of magicians names. Because the
#original list will be unchanged, return the new list and store it in a separate list.
#Call show_magicians() with each list to show that you have one list of the original
#names and one list with the Great added to each magician name.
def make_great(magicians):
	newlist = []
	while magicians:
		newlist.append(magicians.pop()+' the Great')
	return newlist

magicians_2 = make_great(magicians[:])
print('old list')
show_magicians(magicians)
print('new list')
show_magicians(magicians_2)

#8-12. Sandwiches: Write a function that accepts a list of items a person wants
#on a sandwich. The function should have one parameter that collects as many
#items as the function call provides, and it should print a summary of the sandwich
#that is being ordered. Call the function three times, using a different number
#of arguments each time.
print('\n\n--------------------8-12\n\n')

def sandwich(*items):
	print('your sandwich:')
	for item in items:
		print(item)
sandwich('apple', 'tomato', 'cabbage')
sandwich('apple', 'bananna')
sandwich('cinnamon')

print('-------------------------thansk')

#8-13. User Profile: Start with a copy of user_profile.py from page 153. Build
#a profile of yourself by calling build_profile(), using your first and last names
##and three other key-value pairs that describe you.
def build_profile(first, last, **user_info):
	"""Build a dictionary containing everything we know about a user."""
	profile = {}
	profile['first_name'] = first
	profile['last_name'] = last
	for key, value in user_info.items():
		profile[key] = value
	return profile

user_profile = build_profile('albert', 'einstein', location='princeton', field='physics')
print(user_profile)

user_profile = build_profile('alice', 'carroll')
print(user_profile)

#8-14. Cars: Write a function that stores information about a car in a dictionary.
#The function should always receive a manufacturer and a model name. It
#should then accept an arbitrary number of keyword arguments. Call the function
#with the required information and two other name-value pairs, such as a
#color or an optional feature. Your function should work for a call like this one:
##car = make_car(subaru', 'outback', color='blue', tow_package=True)
#Print the dictionary thats returned to make sure all the information was
#stored correctly.
def store_car(manufacturer, model, **keywords):
	car = {}
	car['manufacturer'] = manufacturer
	car['model']= model
	for key, value in keywords.items():
		car[key] = value
	return car

print(store_car('subaru', 'outback', color = 'blue', tow = True))
#8-15. Printing Models: Put the functions for the example print_models.py in a
#separate file called printing_functions.py. Write an import statement at the top
#of print_models.py, and modify the file to use the imported functions.


#8-16. Imports: Using a program you wrote that has one function in it, store that
#function in a separate file. Import the function into your main program file, and
#call the function using each of these approaches:
#import module_name
#from module_name import function_name
#from module_name import function_name as fn
#import module_name as mn
#from module_name import *


#8-17. Styling Functions: Choose any three programs you wrote for this chapter,
#and make sure they follow the styling guidelines described in this section.
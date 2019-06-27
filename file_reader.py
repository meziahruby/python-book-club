with open('pi_digits.txt') as file_object:
	contents = file_object.read()
	print(contents)


# 10-1 Learning Python
print('\nThis is attempt 1, inside the brackets with a line-by-line approach followed by an entire file approach')
with open('learning_python.txt') as file_object:
	for line in file_object:
		print(line)
	print('Let us go with a whole file approach')
	contents = file_object.read()
	print('contents in file are')
	print(contents)
	print('end contents')
	print(contents+'go one')

print('\nThis is attempt 2, inside the brackets')
with open('learning_python.txt') as file_object:
	for line in file_object:
		print(line.rstrip())

print('\nThis is attempt 3, outside the brackets')
with open('learning_python.txt') as file_object:
	my_lines = ''
	for line in file_object:
		my_lines += line
		
print(my_lines)
#

# 10-2 Learning C
print('\nExercise 10-2')
with open('learning_python.txt') as file_object:
	contents = file_object.read()
	print(contents.replace('python','C'))
	
# 10-5 Programming Poll
print('\nProgramming Poll. Write a file with reasons you love programming! Enter "q" to exit.')
while 1:
	new_reason = 'q'
	#new_reason = input('Why do you like programming?: ')
	if new_reason == 'q':
		break
	else: 
		with open('programming_reasons.txt','a') as reasons:
			reasons.write(new_reason+'\n')
			
# 10-6 Addition
total = 0
value_add = 0
print('we are adding numbers. type "q" to exit.')
while 1:
	#value_add = input('Type what value to add to the stash: ')
	value_add = 'q'
	if value_add == 'q':
		break
	try: 
		total += int(value_add)
	except ValueError:
		print('Give me numbers, ya dummy! No words!')
	else:
		print('the running total is ' + str(total))
		
# 10-10 Common Words
with open('rainbow_bridge.txt') as bridge:
	bridge_contents = bridge.read()
print('the book has ' + str(bridge_contents.count('the')) + ' instances of "the"')
lower_bridge_contents = bridge_contents.lower()
print('the book has ' + str(lower_bridge_contents.count('the')) + ' instances of "the"')


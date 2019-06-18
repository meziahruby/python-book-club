from random import randint

class Die():
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

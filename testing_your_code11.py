# 11-1 City, Country, and 11-2 Population

import unittest
from city_functions import city_country
#Define our class to contain our test case
class NamesTestCase(unittest.TestCase):
	#must import unittest.TestCase to know how to run tests
	"""Tests for 'city_country'."""
	
	def test_city_country(self):
		"""Do names like Madrid, Spain work?"""
		formatted_country = city_country('madrid','spain')
		self.assertEqual(formatted_country, 'Madrid, Spain')
		#assertEqual is a method from the unittest module.
		
	def test_city_country_population(self):
		"""Does input like Madrid, Spain - population 500000 work?"""
		formatted_country = city_country('madrid','spain', 500000)
		self.assertEqual(formatted_country, 'Madrid, Spain - population 500000.')
		#assertEqual is a method from the unittest module.
		
#unittest.main()

# 11-3 Employee
# define a class Employee
class Employee():
	"""Simulate a real employee at Bechtel Corporation"""
	
	# initialize FN, LN, Salary
	def __init__(self, first_name, last_name, salary):
		"""Initialize the attributes for an employee instance"""
		self.first_name = first_name
		self.last_name = last_name
		self.salary = salary

# write a method to give a raise
	def give_raise(self, amount_raise = 5000):
		self.salary += amount_raise

# Test the case for give default and custom raise

class TestEmployeeClass(unittest.TestCase):
	"""Tests for raises given to this employee, default and custom."""
	
	def setUp(self):
		"""Create an employee with a salary"""
		self.kevin_employee = Employee("Kevin","Moy",75000)
		
	def test_raise_default(self):
		"""Test Kevin can get a default raise of 5000"""
		self.kevin_employee.give_raise()
		self.assertEqual(self.kevin_employee.salary,80000)
		
	def test_raise_custom(self):
		"""Test Kevin can get his real raise from 2018-2019"""
		self.kevin_employee.give_raise(-1)
		self.assertEqual(self.kevin_employee.salary,74999)
		# Notice that this did not give a raise from the amount in test_raise_default
		# instead, it gave a raise from the setUp parameters
		# Also, if you fail this test, it appears as the third test. Weird, right?
unittest.main()

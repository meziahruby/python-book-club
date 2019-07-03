class Employee():
    """A simple employee"""

    default_raise_amount = 5000

    def __init__(self, first_name, last_name, annual_salary):
        self.first_name = first_name
        self.last_name = last_name
        self.annual_salary = annual_salary
    
    def give_raise(self, raise_amount=default_raise_amount):
        self.raise_amount = raise_amount
        self.annual_salary += self.raise_amount
    

# # Instance of employee class
# employee_B = Employee('Mark', 'Zuckerberg', 350000)
# print(employee_B.annual_salary) # 350,000
# employee_B.give_raise()
# print(employee_B.annual_salary) # 355,000
# employee_B.give_raise(2500)
# print(employee_B.annual_salary) # 357,500
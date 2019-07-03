import unittest
from employee_class_chapter_11 import Employee

class EmployeeTestCase(unittest.TestCase):
    """Tests for 'employee_class_chapter_11.py'"""

    def setUp(self):
        """Create instance of employee class"""
        self.employee_A = Employee('Elon', 'Musk', 300000)
        self.default_raise_amount = 5000

    def test_give_default_raise(self):
        """Test that the default annual raise given to employee is correct"""
        self.employee_A.give_raise()
        self.assertEqual(self.default_raise_amount, self.employee_A.raise_amount)

    def test_give_custom_raise(self):
        """Test that annual raise can be correctly customized to 7500 and given to employee"""
        self.employee_A.give_raise(7500)
        self.assertEqual(7500, self.employee_A.raise_amount)

unittest.main()

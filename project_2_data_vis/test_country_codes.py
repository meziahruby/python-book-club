# 16-4 Testing country_codes module

import unittest
from country_codes import get_country_code

class CountryCodeTestClass(unittest.TestCase):
    """Tests for country_codes.py"""

    def test_get_country_code(self):
        country_code = get_country_code('United Arab Emirates')
        self.assertEqual('ae', country_code)

unittest.main()

# Manually test get_country_code
# print(get_country_code('Andorra')) # ad
# print(get_country_code('United Arab Emirates')) # ae
# print(get_country_code('Afghanistan')) # af

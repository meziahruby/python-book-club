import unittest
from city_functions import format_city_country

class CityCountryTestCase(unittest.TestCase):
    """Tests for 'city_functions.py'"""

    def test_city_country(self):
        """Test if inputting 'Santiago' and 'Chile' returns 'Santiago, Chile'"""
        formatted_city_country = format_city_country('Santiago', 'Chile')
        self.assertEqual(formatted_city_country, 'Santiago, Chile')

    def test_city_country_population(self):
        """Test if inputting city, country, and population gets formatted result"""
        formatted_city_country_population = format_city_country('Santiago', 'Chile', 5000000)
        self.assertEqual(formatted_city_country_population, 'Santiago, Chile - population 5000000')

unittest.main()
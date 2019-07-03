# 11-1 Create City, Country formatting function

# 11-2 Update function for population input and output
# test_city_country in test_cities.py fails if population parameter is added without modifying function
# for test_city_country to work again, population needs to be changed to an optional parameter

def format_city_country(city, country, population=None):
    """Formats city and country information into more readable format"""
    
    if population == None:
        result = f"{city.title()}, {country.title()}"
    else:
        result = f"{city.title()}, {country.title()} - population {population}"
    return result

    
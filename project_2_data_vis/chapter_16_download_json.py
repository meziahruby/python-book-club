# Updates to Python Crash Course Chapter 16 exercises
# https://ehmatthes.github.io/pcc/chapter_16/README.html

import json
from country_codes import get_country_code
from pygal.maps.world import World # instead of import pygal


# 16-5 All Countries

filename = 'population_data.json'
with open(filename) as f:
    population_data = json.load(f)
    # # View first entry in json data
    # print(population_data[0])

# Create dictionary of country names and population for pygal_world_map argument
cc_populations = {}
for population_dict in population_data:
    if population_dict['Year'] == '2010':
        country_name = population_dict['Country Name']
        population = int(float(population_dict['Value']))
        code = get_country_code(country_name)
        if code:
            cc_populations[code] = population
        else:
            print(f"ERROR - {country_name}")

# Plot worldmap of country populations
wm = World()
wm.title = 'World Population in 2010, by Country'
wm.add('2010', cc_populations)

wm.render_to_file('world_population.svg')


# 16-6 GDP

filename = "gdp.json"
with open(filename) as f:
    gdp_data = json.load(f)
    # # View last entry in json data
    # # 2016 is the most recent year for data
    # # Years are not stored as strings!! - Keep in mind for if-block in for loop below
    print (gdp_data[-1])

# Create dictionary of country names and gdp for pygal_world_map argument
cc_gdp = {}
for gdp_dict in gdp_data:
    if gdp_dict['Year'] == 2016:
        country_name = gdp_dict['Country Name']
        gdp = float(gdp_dict['Value'])
        code = get_country_code(country_name)
        if code:
            cc_gdp[code] = gdp
        else:
            print(f"ERROR - {country_name}")

# Plot worldmap of country gdp
wm = World()
wm.title = "World GDP in 2016, by Country"
wm.add('2016', cc_gdp)

wm.render_to_file('world_gdp.svg')

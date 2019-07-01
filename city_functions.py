# 11-1 City, Country
def city_country(city, country, population=''):
	if population:
		return(f'{city.title()}, {country.title()} - population {str(population)}.')
	else:
		return(f'{city.title()}, {country.title()}')



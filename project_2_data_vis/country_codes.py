from pygal.maps.world import COUNTRIES # instead of from pygal.i18n import COUNTRIES

def get_country_code(country_name):
    """Return the Pygal 2-digit country code for given country."""

    for code, name in COUNTRIES.items():
        if name == country_name:
            return code

    if country_name == 'Yemen, Rep.':
        return 'ye'
    elif country_name == 'Vietnam':
        return 'vn'
    elif country_name == 'Venezuela, RB':
        return 've'
    elif country_name == 'Korea, Rep.':
        return 'kr'
    elif country_name == 'Korea, Dem. Rep.':
        return 'kp'
    elif country_name == 'Lao PDR':
        return 'la'

    # If country wasn't found, return None.
    return None


def display_message():
    """Displays a simple message"""
    print("I am learning about functions in this chapter!")


def favorite_book(title):
    """Displays one's favorite book given the title"""
    print(f"One of my favorite books is {title}.")


# def make_shirt(size, text):
#     """Displays summary (size and text) of t-shirt being made"""
#     print(f'This shirt is a size {size}, and has the printed message, "{text}."')


def make_shirt(size="large", text="I love Python"):
    """Displays summary (size and text) of t-shirt being made"""
    print(f'This shirt is a size {size}, and has the printed message, "{text}."')


def describe_city(city, country="the U.S."):
    """Displays the country that a city is in"""
    print(f"{city.title()} is in {country}.")


def city_country(city, country):
    """Returns string of City, Country"""
    return f"{city}, {country}"


def make_album(artist_name, album_title, number_of_tracks=""):
    """Returns dictionary of album information"""
    album = {'artist name': artist_name, 'album title': album_title}

    if number_of_tracks:
        album['number of tracks'] = number_of_tracks

    return album


def show_magicians(magicians):
    """Prints the same of each magician in a list"""
    for magician in magicians:
        print(f"{magician} is a magician! How magical!")


def make_great(magicians):
    """Adds 'the Great' to each magician in a list, and then returns the list"""
    for i, magician in enumerate(magicians):
        magician = magician + " the Great"
        magicians[i] = magician
    return magicians


def make_sandwich(*sandwich_items):
    """Displays summary of items in a sandwich"""
    print("\n" "This sandwich has the following item(s):")
    for item in sandwich_items:
        print(f"- {item}")


def make_car(manufacturer, model, **characteristics):
    """Returns dictionary of car characteristics"""
    car = {'manufacturer': manufacturer, 'model': model}
    
    for characteristic, value in characteristics.items():
        car[characteristic] = value

    return car



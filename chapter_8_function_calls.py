from chapter_8_module import *


# 8-1
display_message()


# 8-2
favorite_book("Ender's Game")


# 8-3
make_shirt("small", "I like cats") # call function using positional arguments
make_shirt(text="Boba is life", size="large") # call function using keyword arguments


# 8-4
make_shirt()
make_shirt(size="medium")
make_shirt(size="small", text="This is a t-shirt")


# 8-5
describe_city("San Francisco")
describe_city("Kyoto", "Japan")
describe_city("Taipei", "Taiwan")


# 8-6
print(city_country("Sacramento", "U.S.A."))
print(city_country("Penzberg", "Germany"))
print(city_country("Basel", "Switzerland"))


# 8-7
print(make_album('Sam Tsui', 'Trust'))
print(make_album('Tori Kelly', 'Unbrekaable Smile'))
print(make_album('AJ Rafael', 'Red Roses'))
print(make_album('AJ Rafael', 'Red Roses', 8))


# 8-8
while True:
    print("\n" "I'd love to hear about one of your favorite albums!")
    print("(Or you can enter 'q' at any time to quit)")
    print("Please tell me...")

    artist_name = input("What is the artist\'s name? ")
    if artist_name == 'q':
        break

    album_title = input("What is the title of one of their albums? ")
    if album_title == 'q':
        break

    print(make_album(artist_name, album_title))


# 8-9
print('\n' '8-9 The OG magicians')
magicians = ["Houdini", "Dark Magician", "Harry Potter"]
show_magicians(magicians)


# 8-10
print('\n' '8-10 The great magicians')
make_great(magicians)
show_magicians(magicians)


# 8-11
print('\n' '8-11 The OG and the great magicians again')
great_magicians = make_great(magicians[:])
show_magicians(magicians)
print('')
show_magicians(great_magicians)


# 8-12
make_sandwich('egg', 'meat')
make_sandwich("ham", "cheese", "tomato")
make_sandwich("avocado", "lettuce", "mayonnaise", "extra veggies")


# 8-14
car = make_car('subaru', 'outback', color='blue', tow_package=True)
print(car)


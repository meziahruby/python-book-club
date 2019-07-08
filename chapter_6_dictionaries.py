# Chapter 6 - Dictionaries

# 6-7. People: List of Dictionaries

person_1 = {
    "name": "Bob",
    "favorite food": "sushi",
    "dream vacation": "Tokyo",
    "age": 24,
}

person_2 = {
    "name": "Ash",
    "favorite food": "ice cream",
    "dream vacation": "Hong Kong",
    "age": 19,
}

person_3 = {
    "name": "Joe",
    "favorite food": "boba",
    "dream vacation": "Taipei",
    "age": 22,
}

people = [person_1, person_2, person_3]

for person in people:
    name = person['name']    
    print(f'This is {name}.')

    for key, value in person.items():
        if key != "name":
            print(f'{name}\'s {key} is {value}.')


# 6-7 People - remix: Dictionary of dictionaries

people = {
    "Bob": {
        "favorite food": "sushi",
        "age": 24,
    },
    "Ash": {
        "favorite food": "ice cream",
        "age": 19,
    }
}

people['Ash']['dream vacation'] = 'London' # 6-12 Extensions: Modifying an existing dictionary

for name, details in people.items():
    print(f'This is {name} again.')

    for key, value in details.items():
        print(f'{name}\'s {key} is {value}.')

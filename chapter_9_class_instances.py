from chapter_9_classes_module import Restaurant, User


# # 9-1
# tasty_pot = Restaurant("Tasty Pot", "hotpot")
# print(tasty_pot.restaurant_name)
# print(tasty_pot.cuisine_type)
# tasty_pot.desecribe_restaurant()
# tasty_pot.open_restaurant()


# # 9-2
# bonchon = Restaurant("Bonchon", "Korean")
# bonchon.desecribe_restaurant()

# marugame = Restaurant("Marugame", "Japanese")
# marugame.desecribe_restaurant()

# guads = Restaurant("Taqueria Guadalajara", "Mexican")
# guads.desecribe_restaurant()


# # 9-3
# user_a = User("Jeremy", "Lin", 30, "male")
# user_a.describe_user()
# user_a.greet_user()

# user_b = User("Taylor", "Swift", 25, "Female")
# user_b.describe_user()
# user_b.greet_user()

# user_c = User("Alex", "Wong", 34, "NA")
# user_c.describe_user()
# user_c.greet_user()


# # 9-4
# restaurant_a = Restaurant("In 'n Out", "American")
# print(restaurant_a.number_served)

# restaurant_a.number_served = 20
# print(restaurant_a.number_served)

# restaurant_a.set_number_served(30)
# print(restaurant_a.number_served)

# restaurant_a.increment_number_served(-5)
# print(restaurant_a.number_served)


# 9-5
user_d = User("Billy", "Bean", 15, "male")
print(user_d.login_attempts) # 0

user_d.increment_login_attempts()
user_d.increment_login_attempts()
user_d.increment_login_attempts()
print(user_d.login_attempts) # 3

user_d.reset_login_attempts()
print(user_d.login_attempts) # 0

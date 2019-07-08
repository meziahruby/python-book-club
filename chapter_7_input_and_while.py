# Chapter 7 - User Input and While Loops
 
# # 7-10. Dream Vacation: User input practice

# dream_vacation = input(
#     "If you could visit one place in the world, "
#     "where would you go? "
#     )

# print(f'That\'s so cool! {dream_vacation.title()} seems awesome!')


# # 7-8. Deli: While looping through lists

# sandwich_orders = [
#     "banh mi", 
#     "katsu sando", 
#     "eggo sandwich",
#     ]

# finished_sandwiches = []

# while sandwich_orders:
#     current_sandwich = sandwich_orders.pop()
#     print(f'I made your {current_sandwich}. Here you go!')
#     finished_sandwiches.append(current_sandwich)

# print('\n' 'These were all the sandwiches made:')
# for sandwich in finished_sandwiches:
#     print(sandwich)


# 7-4. Pizza Toppings: prompt user for input until flagged

prompt = str("What topping would you like to add on your pizza?"
             "\n" + "Enter 'quit' to stop adding toppings. ")

flag = True
total_toppings = []

while flag:
    pizza_order = input(prompt)

    if pizza_order.lower() == 'quit':
        flag = False
    else:
        print(f'Got it, I\'ll add {pizza_order}.' '\n')
        total_toppings.append(pizza_order)

if len(total_toppings) == 0:
    print('\n' 'Alright, one regular pizza coming up!')
else:
    print('\n' 'Ok, your pizza will be out shortly! Final toppings are:')
    for topping in total_toppings:
        print(topping)

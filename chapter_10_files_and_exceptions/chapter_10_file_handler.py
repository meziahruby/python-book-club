# # filename for 10-1 and 10-2
# filename = "learningpython.txt"

# # 10-1: Print contexts of text file
# # Method 1: read in entire file
# with open(filename) as file_object:
#     contents = file_object.read()
#     print(contents.rstrip())

# # Method 2: loop over file object line by line
# with open(filename) as file_object:
#     for line in file_object:
#         print(line.rstrip())

# # Method 3: store lines in list and work with them outside with block
# with open(filename) as file_object:
#     lines = file_object.readlines()

# for line in lines:
#     print(line.rstrip())


# # 10-2
# # read in line by line, and replace "Python" with "C"
# with open(filename) as file_object:
#     lines = file_object.readlines()

# new_language = "C"

# for line in lines:
#     # string method replace does not change the original string (while list method pop does)
#     # need to store modified line in a new variable to print
#     modified_line = line.replace("Python", new_language)
#     print(modified_line.rstrip())


# # 10-3
# guest_name = input("Hello Guest, what is your name? ")

# filename = "guest.txt"

# with open(filename, "w") as file_object:
#     file_object.write(f"This person is a guest: {guest_name}")


# # 10-4
# prompt = str("Please tell me all the names of your guests, one at a time.\n"
#              "Enter 'q' anytime to quit. ")
# flag = True
# filename = "guest_book.txt"

# while flag:
#     guest_name = input(prompt)

#     if guest_name == "q":
#         flag = False
#     else:
#         print("\n" 
#               f"Hi {guest_name}! I'll add you to the guest list. Anyone else in your party?")

#         with open(filename, "a") as file_object:
#             file_object.write(f"{guest_name}\n")


# # 10-5
# prompt = str("Why do you like programming?\n"
#              "Enter 'q' anytime to quit the poll. ")
# flag = True
# filename = "programming_poll_results.txt"

# while flag:
#     poll_answer = input(prompt)

#     if poll_answer == "q":
#         flag = False
#     else:
#         with open(filename, "a") as file_object:
#             file_object.write(f"{poll_answer}\n")
#         print("\n" 
#               "Cool, your response has been recorded. Any other reasons?")
    

# Chapter 4 - Lists

# import time

# for num in range(1, 10**6):
#     print(num)

# numbers = list(range(1, 10**6 + 1))
# print(min(numbers))
# print(max(numbers))

# start = time.clock()
# print(sum(numbers))
# print(time.clock() - start)

# odd_numbers = list(range(1, 21, 2))
# print(odd_numbers)

# multiples_of_three = list(range(3, 31, 3))
# for multiple in multiples_of_three:
#     print(multiple)

# cubes = []
# for value in range(1, 11):
#     cubes.append(value**3)

# print(cubes)

cubes = list(value**3 for value in range(1, 11))
print(cubes)

print('My first three items in the list are:', cubes[:3])
print('My middle three items in the list are:', cubes[2:5])
print('My last three items in the list are:', cubes[-3:])

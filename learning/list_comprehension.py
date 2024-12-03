#List Comprehension = A concise way to create lists in Python, Compact and
#easier to read that traditional loops [expression for value in iterable if condition]

# doubles = []
# for x in range(1, 11):
#     doubles.append(x * 2)
# print(doubles)


#SAME THING, BUT IN LIST COMPREHENSION BELOW


# doubles = [x * 2 for x in range(1, 11)]
# #other examples:
# triples = [y * 3 for y in range(1, 11)]
# squares = [z * z for z in range(1, 11)]
# print(doubles)
# print(triples)
# print(squares)


# fruits = ["apple", "orange", "banana", "coconut"]
# fruits = [fruit.upper() for fruit in fruits]
# print(fruits)
# #"fruit" is our itorator, this prints the fruits in uppercase.

# fruits = ["apple", "orange", "banana", "coconut"]
# fruit_chars = [fruit[1] for fruit in fruits]
# print(fruit_chars)
#prints out the first letter of each fruit, can type 1 to get 2nd letter


# numbers = [1, -2, 3, -4, 5, -6]
# posotive_nums = [num for num in numbers if num >= 0]
# print(posotive_nums)
# #prints the posotive numbers in the list

# numbers = [1, -2, 3, -4, 5, -6]
# negative_nums = [num for num in numbers if num < 0]
# print(negative_nums)
# #prints negetive numbers

# numbers = [1, -2, 3, -4, 5, -6]
# even_nums = [num for num in numbers if num % 2 == 0]
# print(even_nums)
# #prints even numbers

# numbers = [1, -2, 3, -4, 5, -6]
# odd_nums = [num for num in numbers if num % 2 == 1]
# print(odd_nums)
# #prints odd numbers


grades = [85, 42, 79, 90, 56, 61, 30]
passing_grades = [grade for grade in grades if grade >= 60]
print(passing_grades)



################################################List comprehension###############################################
# List Comprehensions Practice #1
# To do the coding exercise below, you can choose different paths. While the correct path in programming is the one that returns the correct result, I encourage you to try applying list comprehension concepts to begin to assimilate them for the future. They can be very useful in your professional practice!

# Create a square_values list consisting of the numbers in the values list, squared.

# values = [1, 2, 3, 4, 5, 6, 9.5]




# List Comprehensions Practice #2
# To do the coding exercise below, you can choose different paths. While the correct path in programming is the one that returns the correct result, I encourage you to try applying list comprehension concepts to begin to assimilate them for the future. They can be very useful in your professional practice!

# Create an even_values list consisting of the numbers in the values list that (you guessed it!) are even.

# values = [1, 2, 3, 4, 5, 6, 9.5]




# List Comprehensions Practice #3
# To do the coding exercise below, you can choose different paths. While the correct path in programming is the one that returns the correct result, I encourage you to try applying list comprehension concepts to begin to assimilate them for the future. They can be very useful in your professional practice!

# For the following list of temperatures in degrees Fahrenheit, express these same values in a new list of temperature values in degrees Celsius. The conversion between type of units is as follows:

# °C = (°F - 32) * (5/9)

# or expressed in another way:

# (degrees_fahrenheit-32)*(5/9)

# The list of temperatures is as follows:

# temperature_fahrenheit = [32, 212, 275]

# Store this new list in a variable called degrees_celsius









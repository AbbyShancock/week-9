
#zip(*iterable) = aggretable elements from two or more iterables (list, tuples, setes, etc.)
# # creates a zip object with paired elements stored in tuples for each elements.
# usernames = ["Dude", "Bro", "Mister"]
# passwords = ("password", "abc123", "guest")
# #these must be the same length

# # users = dict(zip(usernames, passwords))

# # print(type(users))

# # for key,value in users.items():
# #     print(key+" : "+value)

# #prints:
#     # Dude : password
#     # Bro : abc123
#     # Mister : guest




# #added:
# login_date = ["1/1/2021", "1,2,2021", "1/3/2021"]

# users = dict(zip(usernames,passwords,login_date))

# print(type(users))

# for key,value in users.items():
#      print(key+" : "+value)

######################################### zip in python############################################



# Zip Practice #1
# Print to the screen phrases like the following example:

"The capital of Germany is Berlin"

# Use the zip function, loops, and the following lists of countries and capitals to solve it quickly and efficiently.

capitals = ["Berlin", "Tokyo", "Paris", "Helsinki", "Ottawa", "Canberra"]
countries = ["Germany", "Japan", "France", "Finland", "Canada", "Australia"]

users = dict(zip(capitals, countries))
print(type(users))
for capitals,countries in users.items():
      print("The capital of "+ countries + " is " + capitals)

# Zip Practice #2
# Create a zip object made up of lists, of a set of brands and products that you prefer, inside the my_zip variable.
brands = ["Nike", "Elf"]
products = ["Shoes", "Makeup"]

my_zip = zip(brands, products)

print(type(my_zip))

for i in my_zip:
    print(i)

# Zip Practice #3
# Create a zip object with the translations of the numbers from 1 to 5 in Spanish, Portuguese and English (in that same order), and then convert the generated object into a list called numbers:

spanish = ["Uno", "Dos", "Tres", "Cuatro", "Cinco"]
portuguese = ["Um", "Dois", "Tres", "Quatro", "Cinco"]
english = ["One", "Two", "Three", "Four", "Five"]

numbers = zip(spanish, portuguese, english)

print(type(numbers))

for i in numbers:
    print(i)

# one / um / one

# two / two / two

# three / three / three

# four / four / four

# five / five / five

# The result should follow the structure:

# [('one', 'um', 'one'), ('two', 'dois', 'two'), ... ]

# 1: uno / um / one
# 2: dos / dois / two
# 3: tres / três / three
# 4: cuatro / quatro / four
# 5: cinco / cinco / five


#######################zip function challenge#####################
# Challenge: Create a list of countries and their capitals, then zip them together and print
# each country with its capital.

# Two lists: countries and capitals


# Use zip to pair countries with their capitals

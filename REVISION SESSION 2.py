# x  = input()
# print("Your name is ",x)

# var2 = input("Enter your name: ")
# print("Name you entered is ",var2)

# x = int(input("Enter first number:"))
# y = int(input("Enter second number:"))
# print(x+y)

# When we use input function, it always takes input as string

#   STRINGS
# Anything inside enclosed between single or double quotation marks is considered a string.


fruit1 = "Apple"
fruit2 = "Orange"

# print(fruit1 + fruit2)
# print("My favourite fruit is",fruit1)

# print('He said , "I want my favourite fruit"',fruit1)

# print(fruit1[3])
# print(fruit2[4])

# for ch in fruit1:
#     print(ch)



#       STRING SLICING AND OPERATIONS ON STRING

# length of string
# String as an array
# Looping through an string


# name1 = "Ashish"
# len1 = len(name1)
# print(len1)


# StringSlicing

# name2 = "ThomsonReuters"

# print(len(name2))
# print(name2[3])
# print(name2[:3])
# Here if the starting index or ending index is not mentioned then by default it is 0
# print(name2[3:])
# print(name2[3:7])
# print("-------------------")

# print(name2[0:-3])
# negative index in string slicing means len(string) - index
# In the above 14 - 3 => 11

# in string slicing the ending index is not included

# for ch in name2:
    # print(ch)

#       STRING METHODS

# len
# upper()
# lower()
# rstrip()
# replace()
# split()
# capitalize()
# center()
# count()
# endswith()
# find
# isalnum
# isalpha
# islower
# isprintable
# isspace
# istitle()
# startswith
# swapcase()
# title()

# strings are immutable in place

a = "!!!,ashish,!!!!!"
print(len(a))
print(a.upper())
print(a.lower())
print(a)
print(a.rstrip("!"))
# rstrip strips(removes) the leading charaters given inside as parameter
print(a.replace("ashish","danny"))
print(a.split(","))

# split method converts the given string at the specified instance and returns it as a list items


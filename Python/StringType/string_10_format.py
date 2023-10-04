
# Formating is sort of a short cut to embed values from other
# data types in to string

# There is 2 ways we could format strings.
# 1. using format method
# ex: we will put curly braces in a string,
# and those curly braces will be replaces by an argumanet that we putin format method

s ="Today weather is {} fahrenheit."
print(s)                               #  today weather is {} fahrenheit.
print(s.format(84))                     #Today weather is 84 fahrenheit.
print(s.format("eighty four"))          # Today weather is eighty four fahrenheit.

# Note! We can use more than one format curly braces
age = int(input("Enter your age:"))
name = input("Enter your name: ")
s2 = "My name is {} and my age is {}"
print(s2.format(name,age))

s3 = "The brand of the laptop is {1}, and model year is {0}:"
print(s3.format(2018,"Linux"))


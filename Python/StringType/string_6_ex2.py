# Ask useer to enter their age
# if they entered bigger than2 digit numbers and if they don't enter a number
# print invalid age
# otherwise print "You still age"

user_age = input("PLease enter your age: ")
# what is the data type of user_age
# how can we understand if there is more than 2 digit?
#A: len(user_age)> 2
b1 = 0 < len(user_age) <= 2  # We make sure user entered than 0 and less than equals 2 characters
# How we can check if the string consist of numbers only?
# user_age == user_age.upper()
# user_age == user_age.lower()
b2 = user_age == user_age.upper() and user_age == user_age.lower()
if b1 and b2:
    print("Your age is ",user_age)
else:
    print("Your age is not valid")    





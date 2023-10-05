
# Ask user to enter the password but there will be a condiitions,
# our condition for a valid password is:
# 1. it has to have an upper case
# 2. it has to have a lower case
# If user provides a valid password: print "your password is valid"
# Otherwise , print" ypur password is not valid

user = input("Enter your password")
# if user equals to user.lower(), it means original consist of all lower cases
# If user equals to user.upper(), it means original consist of all upper cases.
# Do we want any one of situation above to be true?
# A: we dont want both of situation above to be false at the same time
b1 = user != user.lower()
b2 = user != user.upper()
if b1 and b2:
    print( "Your password is valid")
else:
    print("your password is not valid")


    c1 = not user.islower()
# c1 will be True if ALL the letters in user_pass is lower case. 
# c1 will be False if user_pass is not in ALL lower case. 
c2 = not user.isupper() 
# c2 will be True if ALL the letters in user_pass is upper case. 
# c2 will be False if user_pass is not in ALL upper case. 

# 1. it has to have an upper case
# 2. it has to have a lower cas

if c1 and c2:
    print("your password is valid")
else:
    print("your password is NOT valid")


print("Tec".lower()) #tec
print("Tec".islower()) 











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










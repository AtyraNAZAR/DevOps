# Cfeate a program thats asks user an int value, 
# if this int value is even double the number and print out the result.
# If the number is odd printout "You entered an odd number)"

user_num = int(input("Enter the number"))

if user_num % 2 == 0: 
    print(user_num * 2)
elif user_num % 2 != 0:
    print("You entered odd number")   
     
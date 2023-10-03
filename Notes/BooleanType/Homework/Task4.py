num = input("Enter 5 digit numbers: ")
reverse = 0
while num != 0:
    digit = num % 10
    reverse = reverse * 10 + digit
    num //= 10
print("Reverse number is:" + str(reverse))    
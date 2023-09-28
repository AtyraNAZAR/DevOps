# Ask user to enter 2 equal int variables,
# If user enters 2 numbers that are same we will print
# YOu enyterd 2 equal numbers. If user enters 2 different number
# we will print "You didnt follow the instructure"

print("Enter Two numbers below that are equal.")


num1 = int(input("Enter number 1:"))
num2 = int(input("Enter number 2:"))
if num1 == num2:
    print("You entered two equal numbers.")
elif num1 != num2:
     print("You entered no equal numbers")

     # NOTE!: By using ELIF Statement we are telling Python that both conditions
     # can't be TRue, so if 1st condition is True, it doesnt check
     # 2nd  - ELIF contidion.
     #We could say that we use eloif statement for conditions that depend on
     # ech other so either one or the other one is True
     
 
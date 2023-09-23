#create a program that will find each digit just using the variable
#four_digit_num = 9876
#Once fact is the number is always going to be 4 digit.
# 32 % 10 -> 2
# 49 % 10 -> 9
# 101 % 10 -> 1
# 217 % 10 -> 7
# 8 % 10 -> 8
# 93 % 10 -> 3
# Note : Every time finding a remainder with 10 gives us last digit from the number
four_digit_number = 9876
variable = 10
fact = four_digit_number // variable
factR = four_digit_number % variable
print(fact)
print(factR)
fact1= fact // variable
factR2 = fact % variable
print(fact1)
print(factR2)
fact2 = fact1 // variable
factR3 = fact1 % variable
print(factR3)
print(fact2)
fact3 = fact2 // variable
factR4 = fact2 % variable
print(fact3)

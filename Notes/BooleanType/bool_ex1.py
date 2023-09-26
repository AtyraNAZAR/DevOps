# Proble 1: Even or Odd
# We will write a program that prints True when variable 'number' is even,
# print False when the number is odd
# Odd : 1, 3, 5, 7, 9, 11, 13
# Even: 2, 4, 6, 8, 10, 12
number = 105
# Even numbers are perfectly divisible by 2, and odd numbers not.
is_even = number % 2 == 0
print(is_even)
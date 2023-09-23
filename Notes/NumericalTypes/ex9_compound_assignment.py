num = 11
# How can I learn the type of this variable?
print("Type of the variabl num is", type(num))
print("The value of the variable is", num)

num += 30
print("Type of the variabl num is", type(num)) # int
print("The value of the variable is", num)     #41
num *= 2
print("Type of the variable num is", num) # int
print("The value of the variable is", num) # 82

num /= 2
print("Type of the variabl num is", type(num)) # float
print("The value of the variable is", num)     # 41.0

num ** 1
print("Type of the variabl num is", type(num)) #float
print("The value of the variable is", num)     #41.0

num %= 8
print("Type of the variabl num is", type(num)) # float
print("The value of the variable is", num) # 1.0

num //= 1
print("Type of the variabl num is", type(num))  # float
print("The value of the variable is", num)     #1.0

# NoTE: ONCE IT BECOME A FLOAT NO ARITHMETIC OPEratioin going to change
  
# Logical Operators in python
## and Operators
- 'and' operator checks if **all** conditions are True. For ex;
'''py
# Let's write a program to see if a person can drive:
# In order to drive they must be over 16 years old and they must have a valid lincense
 age = 18
 has_license = True
 can_drive = has_license and age > 15 

 '''
 ## or operator
 - 'or' operatorchecks if at least one condition is True.

 '''py
 # A worker can get rest when it is weekend or when it is on holidays.
 is_holiday = True
 is_weekend = False
 can_rest = is_holiday or is_weekend

 ## not operator 
- Reverses the result of a boolean variable. For ex:
```py
b1 = True
b1 = not b1
print (b1) # False
b1 = not b1
print(b1) # True

```

```py
print ( True and not False) # True
print (not True and True) # False 
print ( True and True and True and False) # False 
print (True or False) # True
print (not False or False) # True
print (False or False) # False
print (False and False) # False

# Using both `and` and `or` operator at the same time.
# In python `and` operator will be executed before the or operator. 
print( False or True and False) #  False
#Note: not operator will be executed before the `and` and `or` operators.

```
 
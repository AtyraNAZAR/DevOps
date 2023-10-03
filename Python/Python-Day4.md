#Python Comparison Operators

### 1. Egual to **==**
- Checks if the value of the left is equal to value on the right.
** Example**
''' py
print (11 == 11)
'''
**Output:
### NOte! Comparison operators always result in a boolean value.
- For the code above since 11 is the same as 11 the output of the code will be 'True'.

### 2. Not Equal to **!=**
- Checks if the left side is **not equal to ** right side
'''py
print(6 != '6') # Since text is not be equal to numbers this line will print True
print(6 != 6 ) # Since the both side of equalion is same, this will print False

### 3. Greater Sign **>**
- Checks if the left side of equaltion is bigger than the right side.
'''py
print(5.0 > 5) # False
print(3 > 4)   # False
print(10 > 9)  # True
'''
### 4. Less Sign **>**
- Checks if the left side of equaltion is smaller than the right side.
'''py
print(5.0 < 5) # False
print(3   < 4)   # True bcs 3 is smaller that the 4
print(10 <  9)  # False bcs 10 is not smaller than the 9
'''
### 5. Greater than Equal >= || Less than equal <= > **>**
- Checks if the left side of equaltion is bigger than the right side.
'''py
print(5.0 >= 5) # True bcs the value are equal
print(5.0 <= 5) # True bcs the value are equal
print(3 >= 4)   # True bcs 3 is smaller than the
print(10 >= 9)  #  True bcs 10 is bigger thann 9

'''

## NOte !
- ** Type Matters: **
- When comparing values type of the values also important:
For ex: '5 == "5"' is 'False bcs one is string (text)
the other is a int type.
- ** We can chain the comparison operatos in python**
'''py
print(1 < 2 < 3) # True
'''

##Note!
- 'True' numerically equals to '1' and 'False' numerically equals to '0'.
For ex: 
'''py
print(int(True)) ## 1
print(int(False)) ## 0
# When using comparison operators between bool and int type
# python auto-converts tool type to int.
print(True == 1) # TRue
print(True > False) # True
print(False < 3 ) # True

'''
## Converting Other Types to Bool

- Which function do you think we are going to use to convert other types to boolean?
**bool()** function.
'''py
b = bool(-2)
print(b) # True
b1 = bool(0)
print(b1) # False

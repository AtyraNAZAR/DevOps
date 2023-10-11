# Stores multiple items
# changeable
# duplicates
# len()-> function
# items are indexed, by refering indes we are able to get it
### in order to store multiple objects in a single variable,
### we can use list type. List is 1 of the 4 built-in collection type
ls = ['str', 7, 5.3, True]
print(type(ls))
 # We can access the elements of lists using index numbers
 # Access the 3rd element from the list. (index 2)
item = ls[2]
print(f"Type of variable item is {type(item)}")
# List also has negative indexing.
print(ls[-1])
# ls = ['str', 7, 5.3, True]

# Getting the range of elements from list. 
# This implementation would work similarly to slicing 
# in string. 

items = ls[1:4]

print(f"Type of variable items is {type(items)} and the value of items is {items}")

# After slicing a list, we get another list. 



# ls = ['str', 7, 5.3, True]

for elm in ls:
    print(elm)
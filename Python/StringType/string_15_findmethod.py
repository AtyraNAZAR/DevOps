# Find method will return us the lowest index of a given character
# or sequence of characters
s = "Techtorial Academy"

print(s.find("a")) # -> 8. it counts the number of a
print(type(s.find("a")))  # <class, int>

print(s.find("b")) # -> -1, bcs no b characyter
print(type(s.find("b"))) # < class, 'int'>
print(s.find("de"))  # 14
# When it is given sequence of characters it will 
# return where that sequence starts in string
print(s.find("ac")) # -1
#"AC is not same as ac inpythotn"

# Get techtorial only from s
print(s[ :10])  # use slicing method


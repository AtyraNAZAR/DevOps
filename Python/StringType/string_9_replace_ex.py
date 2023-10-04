# Given a string, print a version where all 
# the “x” have been removed.
# Except an “x” at the very start or
#  end should not be removed.
#Example outputs
# “xxHxix” → “xHix”
# “abxxxcd” → “abcd”
# “xabxxxcdx” → “xabcdx”

st = input("Enter the string: ")
first_str = st[0]
last_str= st[-1]

# Get the string without the first and last letter
mid_str= st[1 : -1].replace('x','')
new_version = first_str + mid_str + last_str
print(new_version)








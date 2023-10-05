#Create a simple python program to print if a given string 
# ends with another given string. 
#For that ask this two strings to user.

st1 = input("Enter a string : ")
st2= input("Enter a string : ")

# Lets check if the s1 ends with s2
condition = st1.endswith(st2)

# Variable condition will be true if S1 ends with S2
# It will be false if s1 doesn't end with s2
# Type of variable condition is
print(type(condition))  # <clas 'bool>
condition2 = st1.startswith(st2)

print("python".endswith("python")) # TRue
print("python".startswith("python")) # TRue

# endswith and startswith methods arew case sensitive.







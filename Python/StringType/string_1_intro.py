# Ask user to create a string
#print the length of the given string, and print the
# 5th letter from string

s = input("Enter the string:")
#what is the length for this string
print(len(s))

#What would be the last(biggest) index number in string above?
biggest_index =len(s)-1
if biggest_index >= 4:
    print(s[4])
else:
    print("Sorry, but there is no biggest number")    
#Which index number we should find in string
#I need to find the letter at index 4
print(s[4]) # this will bring the 5th character in string

# NOTE! If the index nnumber doesn't exist -> INDEXERROR -> will generate
# Refactor this code so that it wouldn't generate an error 
#when user enters a string that doesn't have 4

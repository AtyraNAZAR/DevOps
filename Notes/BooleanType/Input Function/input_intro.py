# Input function allows us to work with dynamic values.
# bcs, values will be given by user when the code runs.
# Input function will always give the data as text(String), so we should convert
# it according what we need using functions like (int(), float(), bool())

# Example of using input function
var1 = int(input("Enter your age"))
print("User's age is", var1)             # This will print user's input.
print(type(var1))       # Type will be <class 'int'> (text)jb

# Print true if the user is older than 21, print false otherwise


is_older = var1 > 21
print("Is user bigger than 21? ",is_older)
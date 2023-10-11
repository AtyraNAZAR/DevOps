# Finding if a string contains another string.
# We can use in operator
# 
s = "techtorial"
if "t" in s :
    print("This line will be executed because string s contains t.")

# Create aa program, and ask user to enter a string.
# # From the input string print only vowel letters. (vowels are a, e, u, i, 0)    
# Create vowel string
s = input("Enter a string:").lower()
vowels =" aeuio"
 # i will create a loop to go through each letter in string
index = 0
while index < len(s):
    # Here after getting the letter I have to check if the current letter is vowel
    if s[index] in vowels:
        print(f"Letter {s[index]} in string is vowel. ")
    index += 1    





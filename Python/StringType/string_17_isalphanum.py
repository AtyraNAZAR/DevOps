
#isalnum()
# This method will return True if, string consists of letters and numbers only
# letters or numbers or combination of both
s = "text"
s1 = "Text1"
s2 = "1234"
s3 = "1!Te"
print(s.isalnum()) # True
print(s1.isalnum()) # True
print(s2.isalnum()) # True
print(s3.isalnum()) # False

# isalpha()
# Will return True if its only Letters
print(s.isalpha()) # True
print(s1.isalpha()) # False
print(s2.isalpha()) # False
print(s3.isalpha()) # False


#isnumeric()
# Will returnn True if string consists only numbers

print(s.isnumeric()) # True
print(s1.isnumeric()) # False
print(s2.isnumeric()) # False
print(s3.isnumeric()) # False

#Return type of this method is boolean
user_age = input("Enter your age")
if user_age.isnumeric():
    print(f"Awesome age {user_age}")
else:
    print(f"{user_age} is Invalid number")    




















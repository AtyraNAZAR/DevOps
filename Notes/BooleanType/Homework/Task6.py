
str1 = input("Enter the first string ")
str2 = input("Enter the second string ")
if len(str1) >= 3 and len(str2) >= 3 and str2.startswith(str1[-3:]):
    print("True")
else:
    print("False")    

# Create a program that calculates the grade letter of students
# Ask user their grade as an int number
# Print 'NOt a valid grade' if the grade is lower than 0 or bigger than 100.
# Print A+ if grade is higher 95
# Print A if grade is btn 85 - 94
# Print B if grade is btn 75 - 84
# Print C if grade is btn 65 - 74
# Print grade doesn't meet expectation when the grade is lower than 65

grade = int(input("Enter the grade:"))
if grade > 100 or grade <0:
    print("Invalid grade")
elif grade > 94:
    print("Grade is A+")
elif 85 <= grade >= 94:
    print("Grade is A")    
elif 85 <= grade <= 94 :
    print("Grade is A")  
elif 84 <= grade <= 75:
    print("Grade is B")   
elif 74 <= grade <=65:
    print("Grade is C")    
elif grade < 65:
  print("grade doesn't meet expectation when the grade is lower than 65") 





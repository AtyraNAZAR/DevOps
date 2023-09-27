year = int(input("Enter the Year"))

# What conditions should this year give me so that I know it is a leap year
# I am looking a for a year number that is divisible by 4 but not 100
#Or it could 

leap_year = year % 4 == 0 and year % 100 != 0 or year % 400 == 0
print("Is the given year leap?", leap_year)

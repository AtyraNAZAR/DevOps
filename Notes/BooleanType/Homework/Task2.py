
money = float(input("Enter the amount of money"))

cents = int(money * 100)

nmuber_of_dollars = cents // 100
cents %= 100

num_quaters = cents // 25
cents %= 10 

num_dime = cents // 10
cents %= 10

num_nicles = cents // 5
cents %= 5

num_pennies = cents
print()


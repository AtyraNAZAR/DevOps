
quaters = int(input("Quaters: "))
dimes = int(input("Dime "))
nicles = int(input("Nicles "))
pennies = int(input("Pennies "))

coins = (quaters * 25) + (dimes * 10) + (nicles * 5) + (pennies * 1)
dollar = coins // 100
cents = coins % 100
print(dollar +"dollar", cents +"cents")


# We should create a program to calculate if there is still a ticket
# for the game tonight. We are given two variables: Capacity of the stadium
# and the amount of tickets sold.
# Print TRue if I can still buy a ticket, False otherwise
# NOTE! User will enter the capacity and amount of tickets sold.

stadium_capacity = int(input("PLease enter the stadium capacity:"))
sold_tickets = int(input("PLease enter the amount of tickets sold:"))
space = stadium_capacity > sold_tickets
print("There is space for the game tonight:", space)

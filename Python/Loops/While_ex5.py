# Given a string from user, print the mirror ends.
# abcjkhhucba -> abc matching from begging and end but mid isn't matching end the loop
# hannah -> hannah
# civic -> civic
# atechtoriala -> only a

user = input("Enter a string to see if its matching: ")
left_to_right = 0
right_to_left = -1
mirror_end = ""
while left_to_right < len(user):
    if user[left_to_right] == user[right_to_left]:
        mirror_end += user[left_to_right]  # you could also assign r_to_l
    else:
        break    
    left_to_right += 1
    right_to_left -+ 1
print(mirror_end)    






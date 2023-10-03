s = 'programming'
print(s[ 2 : 10]) # ogrammin
print(s[ 2 :10 : 2]) # takes 2 steps, count every other letter " ORMI"
print(s[ 1 : 10 : 3]) # rrm
print(s[ 1: 10 : 4]) # ran

# NEGATIVE STEP
print(s[ 1 : 10 : -3]) # nothing, empthy. starts from tight to left and cann't find any variable

#    start   end   step (always include start->index, end -> don't include)

print(s[ 10 : 1 : -3])  # gmr
print(s[ 7 : 0 : -3])  # mrr

t = "techtorial"
print(t[::1]) # techtorial
print(t[::2]) # tctra
print(t[::-1]) # this will return REVERSE
# Negative index in python starts with 1
# Positive index in python starts with 0
pl = "python"
print(pl[-1 : -3]) # positive index right to left =>empthy
print(pl[-1 : ])  # n
print(pl[-1 : 7]) # n
print(pl[ : -3]) # pyt






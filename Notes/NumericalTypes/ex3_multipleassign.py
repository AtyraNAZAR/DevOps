a = b = c = d = 5
#These variables are not dependent on each other.
print("a", a)
print("b", b)
print("c", c)
print("d", d)

print("After reassignment")
a, b, c, d = 4, 5, 2, 6
print("a", a)
print("b", b)
print("c", c)
print("d", d)

#Python always looks for the last assignment to the line it is executing.
print("After reassignment 2 ")
a, b, c, d = 4, "5", 2.1, 6j
print("a", a)
print("b", b)
print("c", c)
print("d", d)
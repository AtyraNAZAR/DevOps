# clice = substring


text = "Python is a programming language"
substr = text[2:6]
print(substr)
print(type(substr))

# Give me the slicing index numbers to get word programming

prg = text[12:23]
print(prg)
print(substr + prg)

str2 = "simple"
print(str2[3:100]) # ending index is not big deal. thats why it doesn't generate the error
print(str2[2000:4000]) # Empty string
print(str2[4:2])       # Empty string -> "OR"

# Slicing function will always work " left to right"
#UNless there is negative steps involved
# Which numerical value will evalute to "false/true " when converted to boolean?

str3 = "DevOps"
b =bool(str3[2:10])
print(b) # True
b =bool(str3[22:1])
print(b) # False

###########
# Omiting (Leaving empthy) starts or end index when using slicing.
# If you omit start index it will start at index 0, and if you omit ending index,
# it will go till end of string

s = "python"
print(s[1 : ]) # "ython"
print(s[ :4])  # "pyth"
print(s[ : ])  # "python"
print("Tech" [ : ]) # "Tech"














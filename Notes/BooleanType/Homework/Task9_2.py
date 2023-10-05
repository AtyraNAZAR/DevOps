# Given a string, if the first or last chars are 'z', 
# print the string without those 'z' chars, and
#  otherwise print the string unchanged.

# "zHiz" → "Hi"
# "zHi" → "Hi"
# "Hziz" → "Hzi"
# "zzHizz" → zHiz

st = input("Enter the string with  z and remove it: ")
st = st.removeprefix("z")
st = st.removesuffix("z")

print(st)
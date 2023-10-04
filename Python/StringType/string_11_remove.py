# removeprefix method will take one string argument
# anhe it will remove  argument from the string if the string ends with argument.
email ="atyra@techtorial.com"
print(email.removeprefix("techtorial")) # since the string doesn't start with techtorial it won't remove it. FROM THE BEGGINING
print(email.removeprefix("atyra"))      #@techtorial.com

print(email.removesuffix("at"))  # REMOES FROM END
# What is the return type of removesuffix and removeprefix method it will return a  new string value
# removeprefix -> removes from start
# removesuffix -> remove from end
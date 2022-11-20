
# if we don't want entire string
str = "word"

print(str[0:3])

#If we want to start from a specific index and continue getting all the remaining characters of the string until the end,
# we can omit specifying the end index, as follows:

str = "word"

print(str[2:])

#If we want to start from 0 and go until a specific index,
# we can simply specify the ending index:

str = "word"
print(str[:2])
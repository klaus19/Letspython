str="word"
s = "A"

concatenated_str = str + "" + s
print(concatenated_str)

#replace() method

new_str = str.replace(str[0],"A")
print(new_str)

#upper case

let_str = str.upper()
print(let_str)

#multiplication operator * with string

st = "Abc"
no = 2

cass = st*no+''
print(cass)

#String built-in methods len()

sentence = "Nikita is amazing"
print(len(sentence))

#strip()
#strip() removes white spaces that can be in the beginning or at the end of a string:

stru = " Hello there "
print(stru.strip())

#split()

sentence = "This is a sentence that is being declared here"
print(sentence.split(" "))

#join()
#join() is the opposite of split(): from an array of strings, it returns a string.

words = ["cat","dog","lark"]

print(" ".join(words))

#count()
#We can use count() to count the number of times a character or a substring appears in a string:

say = "Hi there"

print(say.count("i"))
print(say.count("the"))

#find()
#find() lets us find a character or a substring in a string and returns the index of it.
# In case it does not find it, it will simply return -1:

string = "Hi there"
print(string.find("3"))
print(string.find("H"))

#capitalize()
#capitalize() to covert the first character of a string into uppercase:

string = "hi there"

print(string.capitalize())

#title()
#title() converts starting characters of each word
# (sequences that are separated by white spaces) of a string into uppercase:

st = "hi, there"
print(st.title())

#isUpper()
#isupper() is a method that we can use to check whether all characters in a string are upper case:

string = "are you HERE"
another_string = "YES"

print(string.isupper())
print(another_string.isupper())

#islower()
#islower() similarly checks whether all characters are lower case:

string = "are you HERE"
another_string = "no"

print(string.islower())
print(another_string.islower())

#isalpha()
#isalpha() returns True if all characters in a string are letters of the alphabet:

string = "A1"
another_string = "aA"

print(string.isalpha())
print(another_string.isalpha())

#isdecimal()
#isdecimal() returns True if all characters in a string are numbers

string = "A1"
another_string = "3.31"
yet_another_string = "3431"

print(string.isdecimal())  # False, since it contains 'A'
print(another_string.isdecimal())  # False, since it contains '.'
print(yet_another_string.isdecimal())




# try except error

try:
    5/0
except ZeroDivisionError:
    print("Value cannot be divided by Zero")

my_list = [2,5,3,6]

try:
    print(my_list[6])
except IndexError:
    print('you have used an index that is out of range')

# usage of finally with try except

my_list = ['a', 'b']

try:
    print(my_list[0])
except IndexError:
    print('An IndexError occurred')
finally:
    print('The program is ending. This is going to be executed.')

# try except, else

my_list = ['a', 'b']
try:
    print(my_list[0])
except IndexError:
    print("An index error")
else:
    print("values is being fetched!")

#



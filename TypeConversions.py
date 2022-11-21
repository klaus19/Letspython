# int() :- it is used to round of ay value to integer

l1 = int(4.5)
print(l1)

l2 = int('3')
print(l2)

# usage of try except block
try:

    l3 = int('A')
    print(l3)
except:
    print("Improper values")

    # float() :- used to get decimal values of the number

    t1 = float(6)
    print(t1)

    t2 = float(5.67)
    print(t2)

    t3 = float('4.56')
    print(t3)

    # str() is used to create strings from floats, integer

    int_to_string = str(1)
    print(int_to_string)

    float_to_string = str(4.56)
    print(float_to_string)

    string_to_string = str('4.5')
    print(string_to_string)

    # Other conversions
    # to convert one data structures into another we use following syntax 'destination_type(input_type)'

    # Conversions to list

    book_tuples = ('b1', 'b2', 'b3')
    list_book = list(book_tuples)
    print(list_book)

    list_book[0] = 'abc'
    print(list_book)

    print(len(list_book))

    book_set = {'er', 'ty', 'ui'}
    set_to_list = list(book_set)
    print(set_to_list)

    # dictionary to list
    books_dict = {'1': 'Book 1', '2': 'Book 2', '3': 'Book 3'}
    dict_to_list = list(books_dict)
    print(dict_to_list)

    # dictionary to list and if we want both key and values

    books_dict = {'1': 'Book 1', '2': 'Book 2', '3': 'Book 3'}
    dict_to_list = list(books_dict.items())
    print(dict_to_list)

    # Conversions to tuple using tuple()

    # list
    books_list = ['Book 1', 'Book 2', 'Book 3']
    book_tuple = tuple(books_list)
    print(book_tuple)

    # set

    book_set = {'Book 1', 'Book 2', 'Book 3'}
    book_tuple = tuple(book_set)
    print(book_tuple)

    # dictionary

    book_dict = {'1': 'Book 1', '2': 'Book 2', '3': 'Book 3'}
    book_tuple = tuple(book_dict)
    print(book_tuple)

    # conversions to set

    books_list = ['Book 1', 'Book 2', 'Book 3']
    list_to_set = set(books_list)
    print(list_to_set)

    book_tuple = ('Book 1', 'Book 2', 'Book 3')
    tuple_to_set = set(book_tuple)
    print(tuple_to_set)

    book_dict = {'1': 'Book 1', '2': 'Book 2', '3': 'Book 3'}
    dict_to_set = set(book_dict)
    print(dict_to_set)

    # conversions to dictionaries

    books_tuple_list = [(1, 'Book 1'), (2, 'Book 2'), (3, 'Book 3')]
    tuple_list_to_dict = dict(books_tuple_list)
    print(tuple_list_to_dict)

    books_list_list = [[1, 'book1'], [2, 'book2'], [3, 'book3']]
    list_to_dict = dict(books_list_list)
    print(list_to_dict)

    book_tuple_list = ([1, 'b1'], [2, 'b2'], [3, 'b3'])
    tuple_list_to_set = dict(books_tuple_list)
    print(tuple_list_to_set)

    books_list_list = ([1,'b1'],[2,'b2'],[3,'b3'])
    list_list_to_set = dict(books_list_list)
    print(list_list_to_set)




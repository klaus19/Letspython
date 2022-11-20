students = ["Albert", "Besart", "Fisnik", "Festim", "Gazmend"]
print(students[4])

# Exception handle

try:
    goData: print(students[5])
except IndexError:
    goData = 'null'
    print(goData)

    students.append("Tejas")
    students[0] = "tejas"
    print(students)

    combined_list = [3.45, 2, "tejas"]
    print(combined_list)

    # slicing the list

    str_list = [1, 2, 4, 3]
    print(str_list[0:3])

    my_list = [1, 2, 3, 5, 6, 7]
    print(my_list[3:])

    do_list = [1, 2, 3, 4]
    print(do_list[:2])

    first = [1, 3, 4]
    second = [2, 7]

    third = first + second
    third.sort()  # sorting the list
    print(third)

    # Nesting one list into another

    first_list = [23, "Physics"]
    second_list = [19, "take"]

    third_list = [first_list, second_list]
    print(third_list)

    print(third_list[0][1])  # pHYICS

    # LENGTH OF ARRAYLIST

    me = [1, 2, "te", "jas"]
    print(len(me))

    # append()
    mt = ["te", "ks"]
    mt.append("eng")
    print(mt)

    # insert()
    yup = ['a', 'z']
    yup.insert(1, 't')
    print(yup)

    # pop()
    # removes last element from list
    mup = [1, 6, 7, 'ret']
    mup.pop()
    print(mup)

    mup.pop(1)  # deletes element at index 0
    print(mup)

    moppy = [1, 3, 4, "yet"]  # deletes the index value
    del moppy[1]
    print(moppy)

    del moppy[0:2]  # del:
    print(moppy)

    # reverse()
    list = [1, 3, 4, 5, 8]
    list.reverse()
    print(list)

    # remove()

    lina = [4, 5, 6, 7]
    lina.remove(4)
    print(lina)

    # index_search
    leta = [1, 3, 5, 6]
    print(leta.index(5))

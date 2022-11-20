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

    my_list = [1,2,3,5,6,7]
    print(my_list[3:])

    do_list = [1,2,3,4]
    print(do_list[:2])

    first = [1,3,4]
    second = [2,7]

    third = first+second
    third.sort()  #sorting the list
    print(third)
# 'in' operator

my_list = [1, 5, 6]
print(5 in my_list)

# 'not in' operator

print(7 not in my_list)

# lIST Comprehension

numbers = [3, 5, 6]
numbers_tenfold = []

for number in numbers:
    number = number * 10
    numbers_tenfold.append(number)
    print(numbers_tenfold)

    positive_num = []
    numbers = [-1, 0, 1, -2, -3, -4, 3, 2]  # complete list

    for num in numbers:
        if num > 0:
            positive_num.append(100 + num)
        print(positive_num)

        first = [3, 5, 6]
        second = [50]
        double_list = [first_element +
                       second_element for first_element in first for second_element in second]
        print(double_list)

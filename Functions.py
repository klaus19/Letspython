# declaring a function

def add(first, second):
    sumoTwo = first + second
    sumoTwo = add(2, 3)
    print(sumoTwo)
    return sumoTwo


# finding the numbers in specific range

def finding_range(first_num, second_num):
    a_range = first_num + 1
    result = 0
    while a_range < second_num:
        result += a_range + second_num
        a_range += 1
        result = finding_range(4, 7)
        print(result)
        return result


# multiply in a range

def multiply_in_range(starting_number, ending_number):
    product = 1
    while starting_number < ending_number:
        product = product * starting_number
        starting_number = starting_number + 1
    return product


# Default arguments

def get_user(first_name, last_name=""):
    return f'hI{first_name}{last_name}'

#
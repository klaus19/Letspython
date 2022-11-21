# if else

num = 0
if num > 0:
    print("value is grerater than 0")
elif num == 0:
    print("value is equal to 0")
else:
    print("value is less than 0")

# for loop is python

for num in range(1, 7):
    print(num)

    # while loop in python

    number = 1

    while number < 7:
        print(number)
        number += 1

    # looping through data structures
    # 1) through list
    students = ["tejas", "gabriela", "nIKITA"]

    for stu in students:
        print(stu)

    # 2) through dictionary

    german_to_english_dictionary = {
        "Wasser": "Water",
        "Brot": "Bread",
        "Milch": "Milk"
    }

for key, value in german_to_english_dictionary:
    print("The German word " + key + " means " + value + " in English")

    #Nested for loop

    numbers = [1, 2, 3]
    sum_of_numbers = []  # Empty list

    for first_number in numbers:
        for second_number in numbers:  # Loop through the list and add the numbers
            current_sum = first_number + second_number
            # add current first_number from the first_list to the second_number from the second_list
            sum_of_numbers.append(current_sum)

    print(sum_of_numbers)

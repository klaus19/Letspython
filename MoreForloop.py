# how to stop a for loop

# we can use break

my_list = [-1, 0, 4, 5]
for elem in my_list:
    if elem < 0:
        print("no is negative")
        break

# how to skip an interation
# we can use continue

my_list = [6, 7, -1, 0]
my_sum = 0

for element in my_list:
    if element < 0:  # Do not include negative numbers in the sum
        continue
    my_sum += element

    print(my_sum)

    # pass is used when we don't want to do anything as we haven't completed it

    my_list = [4,5,6]

    for t in my_list:
        pass



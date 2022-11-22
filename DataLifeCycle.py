names = ['tejas', 'gui', 'opi']


def capitalize_names(current_list):
    for i in range(len(current_list)):
        current_list[i]=current_list[i].capitalize()
    print("Inside the function:", current_list)

    return current_list


capitalize_names(names)  # Inside the function: ['Betim', 'Durim', 'Gezim']

print("Outside the function:", names)  # Outside the function: ['Betim', 'Durim', 'Gezim']

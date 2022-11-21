first_set = {1, 2, 4}

# converting a tuple into set

empty_set = set()
first_set = set((1,3,4))

# length of set is calculated by len

print(len(first_set))

# adding new value , use add()

my_set = {1, 2, 3}

my_set.add(5)
print(my_set)

# if we want to add more than one element then use update() where we can add tuple, list or string into the set

loner_set = {1,3,5}

loner_set.update([4,8,9])

print(loner_set)

loner_set.update("ABC")

print(loner_set)

# deleting an element, we can use remove() or discard() methods

lone_wolf = {4,5,6}
lone_wolf.remove(6)
print(lone_wolf)

# remove() will show error if we try to remove an element that is not present in the set,
# to avoid the error we should discard()

frie = {6,7,8}
frie.discard(1)
print(frie)




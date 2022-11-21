# Union

# we can find union of two operators using | or union() operators

by1 = {1,2,3}
by2 = {4,5,6}

by3 = by1 | by2
print(by3)

# Intersection can be found using & or intersection() method, it means to find common elements in both the sets

b1 = {4,5,6}
b2 = {4,8}

third = b1.intersection(b2)
print(third)

# The difference between two sets represents the collection that contains only
# the elements that are in the first set, but not in the second.
#  We can find the difference between two sets using the - operator or the method difference()

l1 = {1,2,3}
l2 = {2,5}

l3 = l1-l2
print(l3)



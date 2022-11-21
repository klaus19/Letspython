german_to_english = {
    "wasser": "water",
    "brot": "bread",
    "Milch": "Milk"
}

# access specific value

brot_translation = german_to_english["brot"]

print(brot_translation)

milch_translation = german_to_english["Milch"]
print(milch_translation)

# We can also get the value of an element in a dictionary using get() and specifying the key of the item that we want
# to get:

print(german_to_english.get("wasser"))

# dictionaries have duplicate values but keys should unique

my_dictionary = dict([
    ('a', 1),
    ('b', 1),
    ('c', 2)
])

# add new values to a dict

words = {'a': 'alfa', 'b': 'beta', 'd': 'delta'}

words['g'] = "tejas"

print(words)

# modify the values to a dict

words = {
    'a': 'alfa',
    'b': 'beta',
    'd': 'delta',
}

words['b'] = 'bravo'
print(words)

# remove elements from a dict

words = {
    'a': 'alfa',
    'b': 'beta',
    'd': 'delta',
}

words.pop('a')

print(words)

# del is used to delete the speciifc key-value pair

words = {
    'a': 'alfa',
    'b': 'beta',
    'd': 'delta',
}

del words['b']

print(words)

# length of dict

words = {
    'a': 'alfa',
    'b': 'beta',
    'd': 'delta',
}

print(len(words))

# Membership

words = {
    'a': 'alfa',
    'b': 'beta',
    'd': 'delta',
}

print('a' in words)
print('z' not in words)

# converting dictionary into tuples we use items() method

points = {
      'Festim':10,
      'Tejas':20,
      'Lion':30
}

elements = points.items()

print(elements)

# modifying the dictionary using comprehension

points_modified = {key: value + 10 for(key,value) in elements}
print(points_modified)







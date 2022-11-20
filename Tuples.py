# Tuples are collections that are ordered and immutable,
# meaning that their content cannot be changed.

vehicles = ("Computer", "Smartphone", "Smart watch", "Tablet")

print(vehicles)

# length
print(len(vehicles))

# access the third index
print(vehicles[3])

# slicing

print(vehicles[:3])

# index of value
print(vehicles.index('Tablet'))

# merge two tuples using + operator

first = ('ladies', "gentleman ", "welcome")

second = (" niks", 'nikita', 'nik')

third = first + second

print(third)

# membership check , we can chekc whether an element is a part of tuple or not using in and not in operators

nikita = ("i", 'love', 'you', 'a lot')
tejas = ('sorry', 'to', 'hurt', 'u')

friends = (nikita, tejas)
print(friends)

print("love" in nikita)
print('hate' in nikita)
print('sadness' not in nikita)

# we cannot modify tuple values directly,
# initially we have to convert it into list and change the value and then re-convert into tuple

soulmates = list(tejas)
soulmates[3] = "you"
tejas = tuple(soulmates)
print(tejas)



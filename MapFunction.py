# map
def cube(x):
    return x * x * x


li = [2, 3, 5]
newlit = list(map(cube, li))
print(newlit)


# filter
def filter_faction(li):
    return li > 4


newfil = list(filter(filter_faction, li))
print(newfil)

# reduce

from functools import reduce

numbers = [1, 2, 3, 4, 5, 6]


def totalsum(x, y):
    return x + y


sum = reduce(lambda x, y: x + y, numbers)
print(sum)



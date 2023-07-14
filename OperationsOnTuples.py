countries = ("spain", "italy", "india", "england", "germany")

# convert tuple to list
temp = list(countries)

# add to list
temp.append("Russia")

# delete to list
temp.pop(2)

# change item
temp[2] = "Finland "

# convert list to tuple
countries = tuple(temp)

# print(type(temp))

# print tuple
print(countries)

colours = ("Black", "Yellow", "Red", "white")

# merge tuple
colourCountry = countries + colours

print(colourCountry)
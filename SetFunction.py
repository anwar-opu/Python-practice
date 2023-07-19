# list
colours = ["black", "yellow", "Green"]
digit = [2, 3, 67, 5, 3, 5, 7, 2, ]
colours.append("white")

digit.sort()
for n in digit:
    print(n)

for colour in colours:
    print(colour)

print(end="\n")
colours.insert(1, "anwar")
for colour in colours:
    print(colour)

# tuple :
numbers = (1, 2, 6, 2, 7, 3, 5, 6, 7, 4, 7,)

for num in numbers:
    print(num)

print(numbers)

if 1 in numbers:
    print("yes")

# sets :

s = {1, 2, False, "anwar", 8, 2}  # duplicate value not show

print(s)

for value in s:
    print(value)

if 5 in s:
    print("yes")

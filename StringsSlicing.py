food = "mango"
foodLength = len(food)

print(foodLength)  # string length
print(food[0:5])  # including 0 but not 5
print(food[1:4])  # including 1 but not 4
print(food[:4])  # including 0 but not 4
print(food[-3:5])  # len(food)-3 = 2 including but not 5
print(food[3:])  # including 3 to 5
print(food[-3:-1])  # len(food)-3 = 2 including and but not len(food)-1 = 4

employee1 = {110: 90, 113: 87, 115: 90, 116: 70}
employee2 = {117: 60, 118: 80, 119: 79}

print(employee1)
print(employee2)

employee1.update(employee2)
print(employee1)

# delete all item from employee1:
employee1.clear()
print(employee1)

# empty dictionary :
employee3 = {}
print(employee3)

# remove one item form dictionary :
employee2 = {117: 60, 118: 80, 119: 79}
employee2.pop(118)
print(employee2)

# remove last item from dictionary :
employee2.popitem()
print(employee2)

# delete dictionary :
employee2 = {117: 60, 118: 80, 119: 79}
# del employee2
# print(employee2)

# delete one item from dictionary :
del employee2[117]

student1 = {200110: 'anwar ', "age ": 24, "GPA": 3.21}
student2 = {200113: 'rukon ', "age ": 27, "GPA": 2.67}

print(student1)
print(student2)

student1.pop(200110)
print(student1)
student2.popitem()
print(student2)

student1.clear()
print(student1)

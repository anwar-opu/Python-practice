l = [25, 35, 7, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(l)
l.append(10)  # add item in list
# sort list
l.sort()
print("sort list: ", l)  # update list print
l.reverse()
print("reverse sort:", l)
print(l.count(7))

# full list update
# m = l
# m[0] = 0
# print(m)
# print(l)

# only m list update
m = l.copy()
m[0] = 0
print(m)
print(l)

# insert item in list:
l.insert(1, 50)
print(l)

# find index
print(l.index(25))

# merge 2 to list / add 2 list  :
n = [100,200,300]
l.extend(n)
print(l)
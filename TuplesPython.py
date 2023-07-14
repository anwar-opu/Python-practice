tup = (1, 2, 3, "Black", "Red", 2, 5)
print(type(tup), tup)

if 1 in tup:
    print("yes 1 in tuple")
else:
    print("no")

print("index :", tup.index(2))
print("count :", tup.count(2))
print("length :", len(tup))

print(tup[1: 3])
print(tup[0: len(tup): 2])
print("print tuple :")
for i in tup:
    print(i)

# search in tuple :
if "Black" in tup:
    print("yes")

else:
    print("No")

# search in string:

if "bla" in "black":
    print("yes")

else:
    print("no")

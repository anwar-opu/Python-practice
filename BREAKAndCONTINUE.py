# using break statement :
num = int(input("enter integer number: "))

for i in range(1, 13):
    if i == 11:
        break
    print(num, "*", i, "=", num * i)

# using continue statement :
num = int(input("enter integer number: "))

for i in range(1, 13):
    if i == 11:
        continue
    print(num, "*", i, "=", num * i)
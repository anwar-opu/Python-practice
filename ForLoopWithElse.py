for i in range(5):
    print(i)

else:
    print("sorry no i")

for i in range(5):
    print(i)
    if i == 3:
        break
else:
    print("sorry no i ")

for x in range(5):
    print(f"iteration no {x} in for loop")
else:
    print("Else block in loop")
print("Out of loop")

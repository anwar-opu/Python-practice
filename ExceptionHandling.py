n = input("Enter the number:")
print(f"multiplication  table of {n} is :")

try:
    for i in range(1, 11):
        print(f"{int(n)} X {i} = {int(n) * i}")

except:
    print("invalid input ")

print("some imp line of code")


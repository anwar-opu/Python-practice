t = int(input())
i = 0
while t:
    n = int(input())
    for i in range(2, n + 1):
        print(i, end=" ")
        if n == i:
            print("1")
    t = t - 1

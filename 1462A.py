from math import ceil
t = int(input())
while t>0 :
    n = int(input())
    x = list(map(int, input().split()))
    j = n
    m = ceil(n / 2)
    # print(m)
    for i in range(0, m):
        # print(x[i],end=" ")
        print(x[i], end=" ")
        j = j - 1
        if i != j:
            print(x[j], end=" ")

    t = t-1
t = int(input())
while t:
    n, m = input().split()
    mul = int(n) * int(m)
    div = mul // 2
    if mul % 2 == 0:
        print(div)
    else:
        print(div + 1)
    t -= 1

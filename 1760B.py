t = int(input())
while t:
    n = input()
    s = input()
    lst = list(s)
    lst.sort()
    # for i in lst:
    # print(i)
    # print(lst[len(s) - 1])
    convertInt = ord(lst[len(s) - 1])
    result = convertInt - 96
    print(result)
    t -= 1

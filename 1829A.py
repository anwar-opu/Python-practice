t = int(input())
while t:
    s = "codeforces"
    s1 = input()
    i = 0
    count = 0
    for i in range(len(s)):
        if s[i] != s1[i]:
            count += 1
        i = i + 1
    print(count)
    t = t - 1

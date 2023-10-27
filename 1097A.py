a = input()
b, c, d, e, f = input().split()
if a[0] == b[0] or a[1] == b[1] or a[0] == c[0] or a[1] == c[1] or a[0] == d[0] or a[1] == d[1] or a[0] == e[0] or a[
    1] == e[1] or a[0] == f[0] or a[1] == f[1]:
    print("YES")
else:
    print("NO")

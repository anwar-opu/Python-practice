#  user define function
a = 9
b = 8
c = 10
d = 14

# gmean = (num1 * num2) / (num1 + num2)
#
# print(gmean)


def calculationGmean(a, b):
    mean = (a * b) / (a + b)
    print(mean)


def IsGeather(a, b):
    if a > b:
        print("first number is geather ")
    else:
        print("second number is geather or equal")


IsGeather(a, b)
calculationGmean(a, b)

IsGeather(c, d)
calculationGmean(c, d)
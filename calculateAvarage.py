import numbers


def isAvg(a, b, c):
    avg = (a + b + c) / 3
    print(avg)


isAvg(3, 2, 5)


def isAvg(a, b):
    avg = (a + b) / 2
    print(avg)


isAvg(5, 5)


def calAvg(*numbers):
    sum = 0
    for i in numbers:
        sum = sum + i
    return sum / len(numbers)


c = calAvg(2, 3, 4, 5)
print(c)


def printNumber(*num):
    for i in num:
        print(i)


printNumber(2, 3, 4, 5)

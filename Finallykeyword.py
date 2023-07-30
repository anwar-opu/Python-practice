# try:
#     l = [1, 3, 5, 7]
#     i = int(input("enter index number :"))
#     print(l[i])
# except ValueError:
#     print("Value invalid ")
# except IndexError:
#     print("Index invalid")
#
# print("always execute")


# def func():
#     try:
#         l = [1, 2, 3, 4, 5, 7]
#         i = int(input("enter index number:"))
#         print(l[i])
#         return 1
#     except ValueError:
#         print("Invalid value")
#         return 0
#     finally:
#         print("always execute this line")
#
#
# x = func()
# print(x)


def add_sum(num1, num2):
    sum = num1 + num2
    return sum


def sub_num(num1, num2):
    sub = num1 - num2
    return sub


try:
    a = int(input("enter 1st number:"))
    b = int(input("enter 2nd number:"))
    print("Sum two number : ",add_sum(a, b))
    print("Subtract two  number", sub_num(a,b))
except ValueError:
    print("Value error please enter invalid number ")
finally:
    print("thank you for your response :-) ")

x = 10  # global variable


def my_function():
    global x  # access global variable
    x = 7
    y = 5  # local variable
    print(y)


my_function()
print(x)
# print(y)

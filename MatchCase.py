# using match case statements:

x = int(input("enter any number 1 between 5 :"))

match x:
    case 1:
        print("one")
    case 2:
        print("two")
    case 3:
        print("three")
    case 4:
        print("four")
    case 5:
        print("five")
    case _ if x == 6:
        print(x, " x is not 6")
    case _ if x == 80:
        print(x, " x is  80")
    case _:
        print(x)
num = int(input("Enter any number: "))
if num >= 0:
    if 0 <= num < 10:
        print("number  is between 0 to 9  ")
    elif 10 <= num < 20:
        print("number  is between 10 to 19 ")
    elif 20 <= num < 40:
        print("number  is between 20 to 39 ")
    else:
        print("number is geather then 40")
else:
    print("this number is negative !!! ")

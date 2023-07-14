import time

timestamp = time.strftime('%H: %M: %S')
print(timestamp)
timestamp = int(time.strftime('%H'))

if 00 <= timestamp < 10:
    print("Good morning")

elif 10 <= timestamp < 16:
    print("Good afternoon ")

elif 16 <= timestamp < 18:
    print("Good evening ")

elif 18 <= timestamp <= 23:
    print("good night ")

print("HOUR :", timestamp)

timestamp = time.strftime('%M')
print("MIN  :",timestamp)

timestamp = time.strftime('%S')
print("SEC  :",timestamp)

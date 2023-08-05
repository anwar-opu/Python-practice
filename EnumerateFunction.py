marks = [10, 30, 50, 70, 35, 60]

# index = 0
# for mark in marks:
#     print(mark)
#     if index == 3:
#         print(" Good result ")
#     index += 1

print("using enumerate function ")
for index, mark in enumerate(marks):
    print(mark)
    if index == 3:
        print("Great result")
    # else :
    #     print(index)
colours = ["black", "blue", "red", 7, "yellow", "white",]
#           [0]     [1]      [2]   [3]

print(colours)
for colour in colours:
    print(colour)
    # for i in colour:
    #     print(i)

#  if else use list item for search item in list
if "black" in colours:
    print("yes")
else:
    print("no")

# search string in string print yes otherwise no
if "yel" in "yellow":
    print("yes")
else:
    print("no")

# jump-index in list

print(colours[:])
print(colours[0: 2])  # [start index : end index ]
print(colours[0::2])  # [start index : end index : jump-index]

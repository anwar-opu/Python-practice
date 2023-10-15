# Get the value of n from the user
n = int(input())

# Get a list of integers from the user
x = list(map(int, input().split()))

# Sort the list in ascending order
x.sort()
win = x[n-1]
temp = x[0]
# Print the sorted list
# for i in range(n):
#     print(x[i])

for i in range(n):
    if win > x[i] > temp:
        temp = x[i]
print(temp)

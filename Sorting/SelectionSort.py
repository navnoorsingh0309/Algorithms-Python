a = [12, 45, 67, 23, 78, 89, 26, 13, 9, 67, 84, 98, 76, 64, 59, 74, 56]
smallest, smallestPos = a[0], 0
for i in range(0, len(a)-1):
    smallest = a[i]
    smallestPos = i
    for j in range(i, len(a)):
        if a[j]<smallest:
            smallest = a[j]
            smallestPos = j
    temp = a[i]
    a[i] = smallest
    a[smallestPos] = temp

for i in range(len(a)):
    print(a[i])

#Time Complexity is O(N^2)

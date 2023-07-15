a = [12, 45, 67, 23, 78, 89, 26, 13, 9, 67, 84, 98, 76, 64, 59, 74, 56]

for i in range(1, len(a)):
    b = a[i]
    j = i-1
    while j>=0 and a[j]>b:
        temp = a[j]
        a[j]=b
        a[j+1]=temp
        j = j-1

for i in range(len(a)):
    print(a[i])

#Time Complexity for worst and average cases is O(N^2) and for best is O(N)

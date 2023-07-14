a = [12, 45, 67, 23, 78, 89, 26, 13, 9, 67, 84, 98, 76, 64, 59, 74, 56]
b = input("Enter Element to search: ")
c = []
for i in range(len(a)):
    if a[i]==int(b):
        c.append(i)
if len(c)>0:
    print(b + " is found in list at positions:")
    for j in range(len(c)):
        print(str(j+1)+". "+str(c[j]+1))

#Time Complexity O(n) as we need to find all occurrences

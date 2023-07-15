a = [12, 45, 67, 23, 78, 89, 26, 13, 9, 67, 84, 98, 76, 64, 59, 74, 56]

def mergeSort(array):
    if len(array)>1:
        mid = len(array)//2

        L = array[:mid]
        R = array[mid:]

        mergeSort(L)
        mergeSort(R)

        Ldn = Rdn = k = 0

        while Ldn<len(L) and Rdn<len(R):
            if L[Ldn] <= R[Rdn]:
                array[k] = L[Ldn]
                Ldn += 1
            else:
                array[k] = R[Rdn]
                Rdn += 1
            k += 1
        
        while Ldn<len(L):
            array[k] = L[Ldn]
            Ldn += 1
            k += 1
        while Rdn<len(R):
            array[k] = R[Rdn]
            Rdn += 1
            k += 1

mergeSort(a)

for i in range(len(a)):
    print(a[i])
    

#Time Complexity O(N logN)

#This algorithm works on sorted data only
c = []
def checkPrev(list, search, currentPos):
   if list[currentPos-1]==search:
      d = checkPrev(list, search, currentPos-1)
      if d!=-1:
         c.append(d)
      return (currentPos-1)
   else:
      return -1
   
def checkNext(list, search, currentPos):
   if list[currentPos+1]==search:
      d = checkNext(list, search, currentPos+1)
      if d!=-1:
         c.append(d)
      return (currentPos+1)
   else:
      return -1
   
a = [9, 12, 13, 23, 26, 45, 56, 59, 64, 67, 67, 67, 67, 67, 74, 76, 78, 84, 89, 98]
b = input("Enter Element to search: ")

low, high= 0, len(a)-1
while low<=high:
   mid = low + (high-low)/2
   if a[int(mid)]==int(b):
      c.append(int(mid))  
      e = checkPrev(a, int(b), int(mid))
      if e!=-1:
         c.append(e)
      e = checkNext(a, int(b), int(mid))
      if e!=-1:
         c.append(e)
      break
   elif a[int(mid)]>int(b):
      high = int(mid) - 1
   else:
      low = int(mid) + 1

if len(c)>0:
    print(b + " is found in list at positions:")
    for j in range(len(c)):
        print(str(j+1)+". "+str(c[j]+1))

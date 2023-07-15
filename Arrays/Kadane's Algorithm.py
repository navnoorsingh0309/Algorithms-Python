#Task is to find Maximum product of n consecutive integers(Question from GeekForGreeks)

from sys import maxsize
a = [-3, 1, -7, -10, 4, 9, 7, -1, 0, -6, 4, -6, 3]

max_so_far = -maxsize-1
max_ending_here = 1

for i in range(0, len(a)):
    max_ending_here = max_ending_here*a[i]
    if max_so_far<max_ending_here:
        max_so_far = max_ending_here
    
    if max_ending_here<0:
        max_ending_here = 1
    
print(max_so_far)

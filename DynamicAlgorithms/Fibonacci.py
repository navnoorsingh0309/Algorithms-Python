#n-n fibonacci with just oneprint statement

a = input("Enter number of integers to add at one time:")
b = input("Enter number of values to print:")
c = []

a = int(a)
b = int(b)

for i in range(a+1):
    if i!=a-1:
        c.append(1)
    else:
        c.append(-(a-2))


for i in range(0, b):
    print(str(c[a])+", ", end="")
    for j in range(0, a):
        c[j] = c[j+1]
    c[a] = 0
    for k in range(0, a):
        c[a] += c[k]

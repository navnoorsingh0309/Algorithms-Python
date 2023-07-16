#Algorithm to find loop in a linked list

class Node:
    def __init__(self, d):
        self.data = d
        self.next = None

head = Node(10)
head.next = Node(20)
head.next.next = Node(30)
head.next.next.next = Node(40)
head.next.next.next.next = Node(50)

temp = head.next.next.next.next
temp.next = head.next

slowPointer = fastPointer = head

while(slowPointer != None and fastPointer!=None and fastPointer.next!=None):
    slowPointer = slowPointer.next
    fastPointer = fastPointer.next.next
    if slowPointer==fastPointer:
        print("Looped")
        break

#Time Complexity is O(N)

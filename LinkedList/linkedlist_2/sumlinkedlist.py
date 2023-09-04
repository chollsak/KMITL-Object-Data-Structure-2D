class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        
class  LinkedList:
    def __init__(self):
        self.head = None
        self.size = 0
        
    def addLeft(self, value):
        new_node = Node(value)
        new_node.next = self.head        
        self.head = new_node
        self.size += 1
    
    def addRight(self, value):
        new_node = Node(value)
        if self.head == None:
            self.head = new_node
            self.size += 1
            return
        cur_node = self.head
        while cur_node.next != None:
            cur_node = cur_node.next
        cur_node.next = new_node
        self.size += 1
    
    def connectList(self, otherList):
        cur_node = self.head
        if self.head == None:
            self.head = otherList.head
            return
        while cur_node.next != None:
            cur_node = cur_node.next
        cur_node.next = otherList.head
        
    def show(self):
        print(f"{self.head.value}", end=" ")
        cur_node = self.head.next
        while cur_node.next != None:
            print(f"{cur_node.value}",end=" ")
            cur_node = cur_node.next
        print(f"{cur_node.value}",end=" ")
        print()

inp = input("Enter Input (L1,L2) : ").split()

l1 = inp[0].split('->')
l2 = inp[1].split('->')

L1 = LinkedList()
L2 = LinkedList()
M = LinkedList()

print("L1    :", end=" ")
for i in l1:
    print(i,end=" ")
    L1.addRight(i)
print()

M.connectList(L1)
    
print("L2    :", end=" ")
for j in l2:
    print(j,end=" ")
    L2.addLeft(j)
    
M.connectList(L2)
print()
print("Merge :", end=" ")
M.show()
class Node:
    def __init__(self, value = None):
        self.value = value
        self.next = None
        self.prev = None
    
class LinkedList:
    def __init__(self, src, des):
        self.head = None
        self.tail = None
        self.src = src
        self.des = des
    
    def add(self, value):
        if self.head == None:
            self.head = Node(value)
            self.tail = self.head
            self.tail.next = self.head
            self.head.prev = self.tail
            
            if self.src == value:
                self.src = self.head
            if self.des == value:
                self.des = self.head
        else:
            new_node = Node(value)
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
            self.tail.next = self.head
            self.head.prev = self.tail
            
            if self.src == value:
                self.src = self.tail
            if self.des == value:
                self.des = self.tail
                            
        
print("***Railway on route***")
inp = input("Input Station name/Source, Destination, Direction(optional): ")
parts = inp.split('/')

list1 = parts[0].split(',')
list2 = parts[1].split(',')

src = list2[0]
des = list2[1]
drt = "FB"

if len(list2) == 3:
    drt = list2[2]

L = LinkedList(src, des)

for i in list1:
    L.add(i)
    
def findPath(srcNode, desNode, drt):
    lst1 = []
    lst2 = []
    
    temp = srcNode
    while temp != desNode:
        lst1.append(temp.value)
        temp = temp.next
    lst1.append(temp.value)
    
    temp = srcNode
    
    while temp != desNode:
        lst2.append(temp.value)
        temp = temp.prev
    lst2.append(temp.value)
    
    forward_drt = len(lst1)
    backward_drt = len(lst2)
    
    if drt == 'F':
        msg = "->".join(lst1)
        print(f"Forward Route: {msg},{forward_drt-1}")
    elif drt == 'B':
        msg = "->".join(lst2)
        print(f"Backward Route: {msg},{backward_drt-1}")
    else:
        if forward_drt > backward_drt:
            msg = "->".join(lst1)
            print(f"forward Route: {msg},{forward_drt-1}")
        elif forward_drt < backward_drt:
            msg = "->".join(lst2)
            print(f"Backward Route: {msg},{backward_drt-1}")
        else:
            msg = "->".join(lst1)
            print(f"Forward Route: {msg},{forward_drt-1}")
            
            msg = "->".join(lst2)
            print(f"Backward Route: {msg},{backward_drt-1}")

findPath(L.src, L.des, drt)
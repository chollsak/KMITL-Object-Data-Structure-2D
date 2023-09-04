class Node:
    def __init__(self, data = None):
        self.data = data
        self.next = None
        self.prev = None

class CircularLinkedList:
    def __init__(self,src,des):
        self.head = None
        self.tail = None
        self.src = src
        self.des = des
        
    def append(self, data):
        if self.head == None:
            self.head = Node(data)
            self.tail = self.head
            self.tail.next = self.head
            self.head.prev = self.tail
            if self.src == data:
                self.src = self.head
            if self.des == data:
                self.des = self.head
        else:
            new_node = Node(data)
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
            self.tail.next = self.head
            self.head.prev = self.tail
            
            if self.src == data:
                self.src = self.tail
            if self.des == data:
                self.des = self.tail
            
# Example usage
print("***Railway on route***")
input_string = input("Input Station name/Source, Destination, Direction(optional): ")
parts = input_string.split('/')

list1 = parts[0].split(',')
list2 = parts[1].split(',')

direction = "FB"
source = list2[0]
destination = list2[1]
if len(list2) == 3:

    direction = list2[2]
    
c = CircularLinkedList(source, destination)

for i in list1:
    c.append(i)

def findPath(srcNode, desNode, dir):
    lst = []
    lst2 = []

    temp = srcNode
    while temp != desNode:
        lst.append(temp.data)
        temp = temp.next
    lst.append(temp.data)

    temp = srcNode
    while temp != desNode:
        lst2.append(temp.data)
        temp = temp.prev
    lst2.append(temp.data)
    
    len1 = len(lst)
    len2 = len(lst2)
    
    if dir == 'F':
        msg = "->".join(lst)
        print(f"Forward Route: {msg},{len1-1}")  
        
    elif dir == 'B':
        msg = "->".join(lst2)
        print(f"Backward Route: {msg},{len2-1}")
        
    elif len1 == len2:
        msg = "->".join(lst)
        print(f"Forward Route: {msg},{len1-1}")  
        
        msg = "->".join(lst2)
        print(f"Backward Route: {msg},{len2-1}")
        
    else:
        if len1 > len2:
            msg = "->".join(lst2)
            print(f"Backward Route: {msg},{len2-1}")
        else:
            msg = "->".join(lst)
            print(f"Forward Route: {msg},{len1-1}")  
            
            


findPath(c.src, c.des, direction)
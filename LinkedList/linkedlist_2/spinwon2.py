class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
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
        
    def show(self, joiner):
        print(self.head.value, end="")
        if self.head == None:
            return
        elif self.head.next == None:
            print()
            return
        cur_node = self.head.next
        while cur_node.next != None:
            print( f" {joiner} {cur_node.value}", end="")
            cur_node = cur_node.next
        print( f" {joiner} {cur_node.value}", end="")
        print()
        
    def connect_list(self, otherlist):
        cur_node = self.head
        if self.head == None:
            self.head = otherlist.head
            return
        while cur_node.next != None:
            cur_node = cur_node.next
        cur_node.next = otherlist.head
        
inp, k = input("Enter the elements of Linked list/group's size: ").split('/')

inp = [e for e in inp.split()] 
k = int(k)

if k <= 0:
    print("No elements in Linked List ? OK!")
if len(inp) == 0:
    print("Group' size should be greater than 0")
if k <= 0 or len(inp) == 0:
    exit()

        
mainList = LinkedList()
og_list = LinkedList()
subList = LinkedList() 
joiner = "<->"

for v in inp:
    if v.isalpha():
        joiner = ">"
    subList.addLeft(v)
    og_list.addRight(v)
    if subList.size == k:
        mainList.connect_list(subList)
        subList = LinkedList() 
    
    
print("Original Linked list: ", end="")
og_list.show(joiner)

print("Modified Linked list: ", end="")
mainList.show(joiner)
class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

    def __str__(self):
        return str(self.data)

    def setNext(self, next):
        self.next = next


class List:
    # Singly linked list ไม่มี header node with head and tail
    
    def __init__(self, head=None):
        if head is None:
            self.head = self.tail = None
            self.size = 0
        else:
            self.head = head
            t = self.head
            self.size = 1
            while t.next is not None:  # locating tail & find size
                t = t.next
                self.size += 1
            self.tail = t

    def __str__(self):
        s = ''
        p = self.head
        while p is not None:
            s += str(p.data)+' '
            p = p.next
        return s

    def __len__(self):
        return self.size

    def append(self, data):
        """ add at the end of list"""
        p = Node(data)
        if self.head is None:  # null list
            self.head = p
        else:
            t = self.head
            while t.next is not None:
                t = t.next
            t.next = p
        self.size += 1

    def add_first(self, data):
        """ add at first of list """
        p = Node(data)
        p.next = self.head
        self.head = p
        self.size += 1

    def merge_reverse(self, other_list):
        current = self.head
        while current.next is not None:
            current = current.next
        current.next = other_list.head
        self.tail = other_list.tail
        self.size += other_list.size

# รับ input จากผู้ใช้
input_string = input("Enter Input (L1,L2) : ")
lists = input_string.split()

list1 = [item for item in lists[0].split("->")]
list2 = [item for item in lists[1].split("->")]

# สร้าง Linked List จาก input
l1 = List()
for data in list1:
    l1.append(data)
print("L1    :",l1)

temp = ' '.join([str(elem) for elem in list2])
print("L2    :",temp)

l2 = List()

for data in list2:
    l2.add_first(data)

# นำ Linked List มาต่อกันแบบกลับหลัง
l1.merge_reverse(l2)

# แสดงผลลัพธ์
print("Merge :", l1)

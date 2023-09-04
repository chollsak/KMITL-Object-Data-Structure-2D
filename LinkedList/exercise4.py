class node:
    def __init__(self,data):
        # *** code ***
        self.data = data
        self.next = None
        self.snext = None
class Snode(node):
    def __init__(self,data):
        # *** code ***
        super().__init__(data)
class link:
    def __init__(self):
        # *** code ***
        self.head = None
    def next_node(self,data):
        # *** code ***
        if self.head == None:
            self.head = data
        else:
            temp = self.head
            while temp.next != None:
                if temp.data == data.data:
                    return
                temp = temp.next
            temp.next = data
        
    def search(self,data):
        # *** code ***
        temp = self.head
        while temp != None:
            if temp.data == data:
                return temp
            temp = temp.next
        return None

    def next_secondary_node(self,n,data):
        # *** code ***
        temp = self.search(n)
        if temp != None:
            if temp.snext == None:
                temp.snext = data
            else:
                temp = temp.snext
                while temp.snext != None:
                    temp = temp.snext
                temp.snext = data

    def show_all(self):
        # *** code ***
        temp = self.head
        while temp != None:
            print(temp.data,end=' : ')
            if temp.snext != None:
                temp1 = temp.snext
                while temp1 != None:
                    print(temp1.data,end=',')
                    temp1 = temp1.snext
            print()
            temp = temp.next

inp = input("input : ").split(",")
l = link()
for i in inp:
    u = i.split(" ")
    if u[0] == "ADN":
        l.next_node(node(u[1]))
    elif u[0] == "ADSN":
        h = u[1].split("-")
        l.next_secondary_node(h[0],Snode(h[1]))
l.show_all()
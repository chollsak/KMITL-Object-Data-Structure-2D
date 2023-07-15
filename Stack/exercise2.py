class Stack:
    def __init__(self, list = None):
        self.items = list if list is not None else []

    def isEmtry(self):
        return len(self.items) == 0    
    
    def push(self, items):
        self.items.append(items)

    def pop(self):
        if not self.isEmtry():
            return self.items.pop()
        else:
            return -1
        
    def peek(self):
        if self.isEmtry():
            raise IndexError("Stack is empty")
        else:
            return self.items[-1]

    def size(self):
        return len(self.items)
    
    def toint(self):
        for i in range(len(self.items)):
            self.items[i] = int(self.items[i])        

def ManageStack(inp):
    s = Stack()

    def A(n):
        s.push(n)
        print("Add = " + str(n))

    def P():
        if s.size() > 0:
            p = s.pop()
            print("Pop = "+str(p))
        else:
            print("-1")

    def D(n):
        d = Stack()
        if not s.isEmtry():
            for i in s.items:
                if i != n:
                    d.push(i)
                else:
                    print("Delete = " + str(i))
            s.items = d.items
        else:
            print("-1")         

    def LD(n):
        ld = Stack()
        li = s.items
        li.reverse()
        if not s.isEmtry():
            for i in s.items:
                if int(i) >= int(n):
                    ld.push(i)
                else:
                    print("Delete = " + str(i) + " Because " + str(i) + " is less than " + str(n))
            ldlist = ld.items
            ldlist.reverse()            
            s.items = ldlist
        else:
            print("-1")    

    def MD(n):
        md = Stack()
        li = s.items
        li.reverse()
        if not s.isEmtry():
            for i in s.items:
                if int(i) <= int(n):
                    md.push(i)
                else:
                    print("Delete = " + str(i) + " Because " + str(i) + " is more than " + str(n))
            mdlist = md.items
            mdlist.reverse()
            s.items = mdlist
        else:
            print("-1")

    for i in inp:
        L = i.split()
        if L[0] == 'A':
            A(L[1])
        elif L[0] == 'P':
            P()
        elif L[0] == 'D':
            D(L[1])
        elif L[0] == 'LD':
            LD(L[1])
        elif L[0] == 'MD':
            MD(L[1])
    
    s.toint()
    print("Value in Stack = " + str(s.items))
            


inp = input("Enter Input : ").split(',')    
ManageStack(inp)
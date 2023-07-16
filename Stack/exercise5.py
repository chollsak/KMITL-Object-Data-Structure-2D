class Stack:
    def __init__(self, list = None):
        self.items = list if list is not None else []

    def isEmptry(self):
        return len(self.items) == 0
    
    def push(self, item):
        self.items.append(item)
    
    def pop(self):
        if self.isEmptry():
            raise IndexError("Stack is empty")
        else:
            return self.items.pop()
    
    def peek(self):
        if self.isEmptry():
            raise IndexError("Stack is empty")
        else:
            return self.items[-1]
        
    def size(self):
        return len(self.items)
    
    def muchroom_bomb(self):
        self.temp = []
        for i in self.items:
            if int(i) % 2 == 0:
                self.temp.append(int(i) - 1)
            else:
                self.temp.append(int(i) + 2)
        self.items = self.temp
    
def checkStack(stack):
    S = Stack()
    if len(stack) == 0:
        return '0'
    else:
        temp = int(stack[len(stack)-1]) 
        S.push(temp)
        for i in range(len(stack)-2,-1,-1):
            if int(stack[i]) > temp:
                temp = int(stack[i])
                S.push(temp)
        return S.size()


s = Stack()
inp = input("Enter Input : ").split(',')
for i in inp:
    l = i.split()
    if l[0] == 'A':
        s.push(l[1])
    elif l[0] == 'B':
        print(checkStack(s.items))
    elif l[0] == 'S':
        s.muchroom_bomb()
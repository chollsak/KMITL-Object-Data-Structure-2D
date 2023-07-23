class Queue :

    def __init__(self, list = None):
        self.time = 0
        if list == None:
            self.items = []
        else:
            self.items = list
        

    def dequeue(self):
        if not self.isEmpty():
            return self.items.pop(0)
        else:
            return -1
        
    def enqueue(self, item):
        self.items.append(item)
    
    def isEmpty(self):
        return len(self.items) == 0
    
    def size(self):
        return len(self.items)
    
    def timeReset(self):
        self.time = 0

    def Time(self):
        return self.time

    def __str__(self) -> str:
        return str(self.items)

def cashier():
    if y.size() + 1 < 6:
        y.enqueue(x.dequeue())
    elif z.size() + 1 < 6:
        z.enqueue(x.dequeue())
    if not y.isEmpty():
        y.time += 1
    if not z.isEmpty():
        z.time += 1

x = Queue()
y = Queue()
z = Queue()

inp = [*input("Enter people : ")]
x.items = inp

for i in range(1, len(inp)+1):
    if not y.isEmpty() and y.time == 3:
        y.dequeue()
        y.timeReset()
    if not z.isEmpty() and z.time == 2:
        z.dequeue()
        z.timeReset()

    cashier()
    print(i,x,y,z)
class Queue:
    def __init__(self, list = None):
        self.time = 0

        if list == None:
            self.items = []
        else:
            self.items = list

    def isEmpty(self):
        return len(self.items) == 0

    def dequeue(self):
        if not self.isEmpty():
            return self.items.pop(0)
        else:
            raise IndexError('Queue is empty')
        
    def enqueue(self, item):
        self.items.append(item)

    def size(self):
        return len(self.items)
    
    def Time(self):
        return self.time
    
    def timeReset(self):
        self.time = 0

    def __str__(self):
        return str(self.items)

def cashier():
    if c_1.size() + 1 < 6:
        c_1.enqueue(main.dequeue())
    elif c_2.size() + 1 < 6:
        c_2.enqueue(main.dequeue())
    
    if not c_1.isEmpty():
        c_1.time += 1
        
    if not c_2.isEmpty():
        c_2.time += 1

main = Queue()
c_1 = Queue()
c_2 = Queue()

inp = [*input("Enter Input : ")]
main.items = inp

for i in range(1, len(inp)+1):
    if not c_1.isEmpty() and c_1.time == 3:
        c_1.dequeue()
        c_1.timeReset()
    if not c_2.isEmpty() and c_2.time == 2:
        c_2.dequeue()
        c_2.timeReset()

    cashier()
    print(i, main, c_1, c_2)

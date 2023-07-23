class Queue:
    def __init__(self, list = None):
        self.error_d = 0
        self.error_inp = 0
        self.last_number = -1
        
        if list == None:
            self.items = []
        else:
            self.items = list
    
    def __str__(self):
        return str(self.items)
    
    def isEmpty(self):
        return len(self.items) == 0
    
    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        if not self.isEmpty():
            return self.items.pop(0)
        else: 
            self.error_d += 1
        
    def size(self):
        return len(self.items)
    
    def peek(self):
        if self.isEmpty():
            return 0
        else:
            return self.items[-1]

def Output(l):
    answer = []
    for i in l:
        answer.append("*%d" %i)
    return answer

q = Queue()
s = Queue()

inp = input('input : ').split(',')
q.items = inp

for i in q.items:
    print("Step : %s" %i)
    j = 0

    if i[j] == 'E' and i[1::1].isdigit():
        n = int(i[1::1])
        if n > 0:
            if s.isEmpty():
                for k in range(s.last_number+1, n+(s.last_number)+1):
                    s.enqueue(k)

            else:
                for k in range(s.peek()+1, int(s.peek())+1+n):
                    s.enqueue(k)
                
            s.last_number = s.peek()

        print("Enqueue :", Output(s.items))

    elif i[j] == 'D' and i[1::1].isdigit():
        nn = int(i[1::1])
        if nn > 0:
            for r in range(0,nn):
                s.dequeue()

        print("Dequeue :", Output(s.items))

    else:
        s.error_inp += 1
        print(Output(s.items))

    print("Error Dequeue : %d" %s.error_d)
    print("Error input : %d" %s.error_inp)
    print('--------------------')



        

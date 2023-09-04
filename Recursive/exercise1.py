class Stack :
    def __init__(self,name) -> None:
        self.items = []
        self.name = name
    def push(self,data):
        self.items.append(data)
    def pop(self):
        return self.items.pop()
    def peek(self):
        return self.items[-1]
    def isEmpty(self):
        return self.items == []
    def size(self):
        return len(self.items)
    def __str__(self) -> str:
        return " ".join(self.items)
    
A = Stack("A")
B = Stack("B")
C = Stack("C")
def move(n,A,B,C,maxn):
    if n == 1:
        display(maxn)
        print(f"move {A.peek()} from  {A.name} to {C.name}")
        # print("n==1")
        # print(f"A : {A} , B : {B} , C : {C}") 
        C.push(A.pop())
        return
    else:
        move(n-1,A,C,B,maxn)
        display(maxn)
        print(f"move {A.peek()} from  {A.name} to {C.name}")
        C.push(A.pop())
        move(n-1,B,A,C,maxn)

def add_number(n):
    if n == 1:
        A.push(str(n))
        return
    A.push(str(n))
    add_number(n-1)

def display(n):
    if n == 0:
        return
    else:
        print(f"{A.items[n-1] if A.size() >= n else '|'}  {B.items[n-1] if B.size() >= n else '|'}  {C.items[n-1] if C.size() >= n else '|'}") 
        display(n-1)
n = int(input("Enter Input : "))
add_number(n)
# print(A)
move(n,A,B,C,n+1)
display(n+1)
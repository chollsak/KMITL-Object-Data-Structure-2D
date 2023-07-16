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
    


def postFixeval(st):    
    s = Stack()

    for token in st:
        if token.isdigit():
            s.push(float(token))
        elif token.startswith('-') and len(token) >= 2:
            s.push(float(token))
        else:
            operand2 = s.pop()
            operand1 = s.pop()
            result = operation_perform(token, operand1, operand2)
            s.push(result)    
    
    return s.pop()

def operation_perform(operator, operand1, operand2):
    if operator == '+':
        return operand1 + operand2
    elif operator == '-':
        return operand1 - operand2
    elif operator == '*':
        return operand1 * operand2
    elif operator == '/':
        return operand1 / operand2
    else:
        return -1


print(" ***Postfix expression calcuation***")

token = list(input("Enter Postfix expression : ").split())
result = postFixeval(token)

print("Answer : ",'{:.2f}'.format(result))
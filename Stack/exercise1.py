'''
 * กลุ่มที่  : 23010016
 * 65010195 ชลศักดิ์ อนุวารีพงษ์
 * chapter : 3	item : 1	ครั้งที่ : 0006
 * Assigned : Tuesday 11th of July 2023 10:10:03 PM --> Submission : Friday 14th of July 2023 05:16:30 AM	
 * Elapsed time : 3306 minutes.
 * filename : exercise1.py
'''

class Stack:
    def __init__(self, lst=None):
        self.items = lst if lst is not None else []

    def is_empty(self):
        return len(self.items) == 0

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        else:
            raise IndexError("Stack is empty")

    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        else:
            raise IndexError("Stack is empty")

    def size(self):
        return len(self.items)


def is_valid(ps):
    opening_case = ['(', '[']
    closing_case = [')', ']']
    stack = Stack()

    for i in ps:
        if i in opening_case:
            stack.push(i)
        elif i in closing_case:
            closing_index = closing_case.index(i)
            if not stack.is_empty() and stack.peek() == opening_case[closing_index]:
                stack.pop()
            else:
                stack.push(i)
    
    return stack.size()


ps = input('Enter Input: ')
unmatch_n = is_valid(ps)

if unmatch_n == 0:
    print(unmatch_n)
    print('Perfect!!!')
else:
    print(unmatch_n)


'''
The difference between if stack and stack[-1] == opening_case[closing_index]: 
and if stack[-1] == opening_case[closing_index]: lies in how they handle the case 
when the stack is empty.

1. if stack and stack[-1] == opening_case[closing_index]:
- This condition checks if the stack is not empty (stack) and if the last element of 
the stack (stack[-1]) matches the expected opening parenthesis or bracket (opening_case[closing_index]).
- If the stack is empty, the first part of the condition (stack) will evaluate to False, 
and the entire condition will be False, resulting in the code inside the else block being executed.

2. if stack[-1] == opening_case[closing_index]:

- This condition checks if the last element of the stack (stack[-1]) matches the 
expected opening parenthesis or bracket (opening_case[closing_index]).
- If the stack is empty and stack[-1] is accessed, it will raise an IndexError 
because there are no elements in an empty list. This will cause the program to terminate with an error.

In summary, the difference is that the first condition (if stack and stack[-1] == opening_case[closing_index]:) 
includes an additional check to ensure that the stack is not empty before accessing stack[-1], 
preventing an IndexError in the case of an empty stack. 
The second condition (if stack[-1] == opening_case[closing_index]:) assumes that the stack is not empty 
and directly accesses stack[-1] without checking, which can cause an error if the stack is empty.'''
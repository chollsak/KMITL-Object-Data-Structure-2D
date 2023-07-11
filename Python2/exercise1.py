'''
 * กลุ่มที่  : 23010016
 * 65010195 ชลศักดิ์ อนุวารีพงษ์
 * chapter : 2	item : 1	ครั้งที่ : 0002
 * Assigned : Tuesday 4th of July 2023 05:13:52 PM --> Submission : Thursday 6th of July 2023 03:55:05 PM	
 * Elapsed time : 2801 minutes.
 * filename : exercise1.py
'''
class Calculator:
    def __init__(self, number):
        self.number = number

    def __add__(self, other):
        return self.number + other.number

    def __sub__(self, other):
        return self.number - other.number

    def __mul__(self, other):
        return self.number * other.number

    def __truediv__(self, other):
        return self.number / other.number


x, y = input("Enter num1 num2 : ").split(",")
x, y = Calculator(int(x)), Calculator(int(y))

print(x + y, x - y, x * y, x / y, sep="\n")

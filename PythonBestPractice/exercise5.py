'''
 * กลุ่มที่  : 23010016
 * 65010195 ชลศักดิ์ อนุวารีพงษ์
 * chapter : 12	item : 5	ครั้งที่ : 0012
 * Assigned : Tuesday 4th of July 2023 11:37:09 AM --> Submission : Tuesday 11th of July 2023 11:16:34 AM	
 * Elapsed time : 10059 minutes.
 * filename : 12-5.py
'''
print(" *** class MyInt ***")

num1, num2 = input("Enter 2 number : ").split()

class MyInt():
    def __init__(self, num):
        self.num = num
    
    def isPrime(self):
        if(self.num <= 1):
            return False
        elif(self.num > 1):
            for i in range(2,self.num):
                if (self.num % i) == 0:
                    return False
            return True

    def showPrime(self):
        show = ""
        if(self.num <= 1):
            show = "!!!A prime number is a natural number greater than 1"
        else:
            for i in range(2, self.num+1):
                if(MyInt(i).isPrime()):
                    show += "{} ".format(i)
                else:
                    pass
        return(show)
                
    def __sub__(self, b):
        return self.num - int(b / 2)
        
n1 = MyInt(int(num1))
n2 = MyInt(int(num2))

print("{} isPrime : {}".format(num1, n1.isPrime()))
print("{} isPrime : {}".format(num2, n2.isPrime()))
print("Prime number between 2 and {} : {}".format(num1,n1.showPrime()))
print("Prime number between 2 and {} : {}".format(num2,n2.showPrime()))
print("{} - {} = {}".format(num1, num2, n1.__sub__(int(num2))))



'''
 * กลุ่มที่  : 23010016
 * 65010195 ชลศักดิ์ อนุวารีพงษ์
 * chapter : 2	item : 5	ครั้งที่ : 0001
 * Assigned : Friday 7th of July 2023 09:53:34 PM --> Submission : Tuesday 11th of July 2023 09:55:35 AM	
 * Elapsed time : 5042 minutes.
 * filename : exercise5.py
'''
class funString():
    def __init__(self, string=""):
        self.string = string

    def __str__(self):
        return self.string

    def size(self):
        return len(self.string)

    def changeSize(self):
        result = ""
        for char in self.string:
            if char.islower():
                result += char.upper()
            elif char.isupper():
                result += char.lower()
            else:
                result += char
        self.string = result
        return self.string

    def reverse(self):
        result = ""
        for i in range(len(self.string) - 1, -1, -1):
            result += self.string[i]
        self.string = result
        return self.string

    def deleteSame(self):
        result = ""
        for char in self.string:
            if char not in result:
                result += char
        self.string = result
        return self.string

str1, str2 = input("Enter String and Number of Function : ").split()
res = funString(str1)

if str2 == "1":
    print(res.size())
elif str2 == "2":
    print(res.changeSize())
elif str2 == "3":
    print(res.reverse())
elif str2 == "4":
    print(res.deleteSame())

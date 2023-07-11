'''
 * กลุ่มที่  : 23010016
 * 65010195 ชลศักดิ์ อนุวารีพงษ์
 * chapter : 2	item : 2	ครั้งที่ : 0002
 * Assigned : Tuesday 4th of July 2023 05:14:04 PM --> Submission : Thursday 6th of July 2023 04:31:09 PM	
 * Elapsed time : 2837 minutes.
 * filename : exercise2.py
'''
class Spherical:    

    def __init__(self,r):
        self.radius = r

    def changeR(self,Radius):
        self.radius = Radius

    def findVolume(self):
        return 4/3*pi*self.radius**3

    def findArea(self):
        return 4*pi*self.radius**2

    def __str__(self):
        return "Radius =" + str(self.radius) + " Volumn = " + str(self.findVolume()) + " Area = " + str(self.findArea()) 
        


pi =  3.1415926535897932384626433832795028841971693993751058209749445923078164062862089986280348253421170679  
r1, r2 = input("Enter R : ").split()
R1 = Spherical(int(r1))
print(type(R1))
print(dir(R1))
print(R1)
R1.changeR(int(r2))
print(R1)
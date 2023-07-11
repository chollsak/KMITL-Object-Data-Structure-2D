'''
 * กลุ่มที่  : 23010016
 * 65010195 ชลศักดิ์ อนุวารีพงษ์
 * chapter : 2	item : 4	ครั้งที่ : 0001
 * Assigned : Friday 7th of July 2023 09:51:41 PM --> Submission : Tuesday 11th of July 2023 11:00:52 AM	
 * Elapsed time : 5109 minutes.
 * filename : exercise4.py
'''
def hbd(age):

    next_div = None

    if age % 2 == 0:
        saimai = 20
        div1 = 2
        div2 = 0
    else:
        saimai = 21
        div1 = 2
        div2 = 1

    base = (age - div2) / div1
   
    return f"saimai is just {saimai}, in base {int(base)}!"

   

       


year = input("Enter year : ")

print(hbd(int(year)))
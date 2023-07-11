'''
 * กลุ่มที่  : 23010016
 * 65010195 ชลศักดิ์ อนุวารีพงษ์
 * chapter : 1	item : 4	ครั้งที่ : 0002
 * Assigned : Tuesday 4th of July 2023 03:28:37 PM --> Submission : Tuesday 4th of July 2023 03:39:57 PM	
 * Elapsed time : 11 minutes.
 * filename : exercise4.py
'''
def odd_list(al):
    income_list = al
    odd_num_list = []
    for num in income_list:
        if num % 2 != 0:
            odd_num_list.append(num)
        else:
            continue
    return odd_num_list      


print(" ***Function Odd List***")
ls = [int(e) for e in input("Enter list numbers : ").split()]
opls = odd_list(ls)
print("Input list : ", ls, "\nOutput list : ", opls)

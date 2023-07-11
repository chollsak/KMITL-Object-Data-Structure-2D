'''
 * กลุ่มที่  : 23010016
 * 65010195 ชลศักดิ์ อนุวารีพงษ์
 * chapter : 1	item : 5	ครั้งที่ : 0002
 * Assigned : Tuesday 4th of July 2023 03:40:23 PM --> Submission : Tuesday 11th of July 2023 10:34:10 AM	
 * Elapsed time : 9773 minutes.
 * filename : exercise5.py
'''
print("*** Fun with countdown ***")
input_lst = input("Enter List : ").split()
cnt_lst = []
temp_lst = []
ans_lst = []
index_cnt = 0


for i in range (len(input_lst)):
    input_lst[i] = int(input_lst[i])


for i in input_lst:
    if temp_lst == [] and i != 1:
        temp_lst.append(i)
    elif temp_lst == [] and i == 1:
        temp_lst.append(i)
        cnt_lst.append(temp_lst.copy())
        temp_lst.clear()
    else:
        if (temp_lst[-1] - 1) == i  and i == 1:
            temp_lst.append(i)
            cnt_lst.append(temp_lst.copy())
            temp_lst.clear()
        elif (temp_lst[-1] - 1) == i and i != 1:
            temp_lst.append(i)
        elif (temp_lst[-1] - 1) != i:  
            temp_lst.clear()
            temp_lst.append(i)

ans_lst.append(cnt_lst.copy())
ans_lst.insert(0, len(cnt_lst))

print(ans_lst)
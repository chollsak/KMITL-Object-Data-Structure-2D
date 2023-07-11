'''
 * กลุ่มที่  : 23010016
 * 65010195 ชลศักดิ์ อนุวารีพงษ์
 * chapter : 1	item : 3	ครั้งที่ : 0002
 * Assigned : Tuesday 4th of July 2023 03:26:23 PM --> Submission : Friday 7th of July 2023 06:13:23 PM	
 * Elapsed time : 4487 minutes.
 * filename : exercise3.py
'''
print("*** Election ***")

scores_list = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
voted_list = []

nocadidatewin = 0

voter = int(input("Enter a number of voter(s) : "))

voted_box = input().split(" ")

for i in voted_box:
    voted_list.append(int(i))

for j in voted_list:
    if j > 20 or j < 0:
        pass
    else:
        scores_list[j] += 1    

for k in scores_list:
    if k == 0:
        nocadidatewin += 1
        if nocadidatewin == 21:
            print("*** No Candidate Wins ***")    
        
             

max_value = max(scores_list)
indexes = [index for index, value in enumerate(scores_list) if value == max_value]

if len(indexes) > 3:
    exit()
else:
    print(*indexes)

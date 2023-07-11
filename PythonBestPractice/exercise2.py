'''
 * กลุ่มที่  : 23010016
 * 65010195 ชลศักดิ์ อนุวารีพงษ์
 * chapter : 12	item : 2	ครั้งที่ : 0004
 * Assigned : Tuesday 4th of July 2023 10:36:53 AM --> Submission : Tuesday 11th of July 2023 11:14:56 AM	
 * Elapsed time : 10118 minutes.
 * filename : 12-2-(X).py
'''
print(" *** Rank score ***")

data = input("Enter ID and Score end with ID : ").split()

student = data.pop()
output = {}

print(data)
print(student)

dataKey = [data[x] for x in range(len(data)-1) if x % 2 == 0]
dataVal = [float(data[x+1]) for x in range(len(data)-1) if x % 2 == 0]

data = dict(zip(dataKey, dataVal))

value_sorted = dict(sorted(data.items(), key=lambda x:x[1], reverse=True))

for k,v in sorted(list(value_sorted.items()), key=lambda t: (-1*t[1], int(t[0]))):
    output[k] = v

print(output)

rank = 0
if student in value_sorted:
    rank = list(value_sorted).index(student) + 1
else: 
    rank = "Not Found"
print(rank)
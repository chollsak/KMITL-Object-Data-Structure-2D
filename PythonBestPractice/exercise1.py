'''
 * กลุ่มที่  : 23010016
 * 65010195 ชลศักดิ์ อนุวารีพงษ์
 * chapter : 12	item : 1	ครั้งที่ : 0003
 * Assigned : Tuesday 4th of July 2023 10:13:50 AM --> Submission : Tuesday 4th of July 2023 10:36:33 AM	
 * Elapsed time : 22 minutes.
 * filename : main.py
'''
print(" *** BMI ***")

weight, height = input("Enter your weight(kg) and height(m) : ").split()

w = float(weight)
h = float(height)

bmi = w/(h*h)

if bmi < 18.5:
    print("Your status is : Below normal weight.")
elif 18.5 <= bmi < 25:
    print("Your status is : Normal weight.")
elif 25 <= bmi < 30:
    print("Your status is : Overweight.")
elif 30 <= bmi < 35:
    print("Your status is : Case I Obesity.")
elif 35 <= bmi < 40:
    print("Your status is : Case II Obesity.")
else:
    print("Your status is : Case III Obesity.")
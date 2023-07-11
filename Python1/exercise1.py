'''
 * กลุ่มที่  : 23010016
 * 65010195 ชลศักดิ์ อนุวารีพงษ์
 * chapter : 1	item : 1	ครั้งที่ : 0002
 * Assigned : Tuesday 4th of July 2023 09:59:11 AM --> Submission : Tuesday 4th of July 2023 03:14:16 PM	
 * Elapsed time : 315 minutes.
 * filename : exercise1.py
'''
print("*** Rabbit & Turtle ***")
d, Vr, Vt, Vf = map(int, input("Enter Input : ").split())

v_diff = Vt-Vr 

time_turtle_to_rabbit = d/v_diff

d_of_fly = time_turtle_to_rabbit * Vf

print("%.2f" %d_of_fly)

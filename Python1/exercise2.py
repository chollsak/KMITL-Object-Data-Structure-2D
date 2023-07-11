'''
 * กลุ่มที่  : 23010016
 * 65010195 ชลศักดิ์ อนุวารีพงษ์
 * chapter : 1	item : 2	ครั้งที่ : 0003
 * Assigned : Tuesday 4th of July 2023 10:04:04 AM --> Submission : Tuesday 4th of July 2023 03:26:17 PM	
 * Elapsed time : 322 minutes.
 * filename : exercise2.py
'''
print(" *** Wind classification ***")
wind_speed = float(input("Enter wind speed (km/h) : "))

list_of_levels = ["Wind classification is ","Breeze.", "Depression.", "Tropical Storm.", "Typhoon.", "Super Typhoon."]

if 0 <= wind_speed <= 51.99:
    print(list_of_levels[0] + list_of_levels[1])
elif 52.00 <= wind_speed <= 55.99:
    print(list_of_levels[0] + list_of_levels[2])
elif 56.00 <= wind_speed <= 101.99:
    print(list_of_levels[0] + list_of_levels[3])
elif 102.00 <= wind_speed <= 208.99:
    print(list_of_levels[0] + list_of_levels[4])
else:
    print(list_of_levels[0] + list_of_levels[5])                

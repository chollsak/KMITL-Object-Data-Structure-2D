'''
 * กลุ่มที่  : 23010016
 * 65010195 ชลศักดิ์ อนุวารีพงษ์
 * chapter : 12	item : 3	ครั้งที่ : 0003
 * Assigned : Tuesday 4th of July 2023 11:36:54 AM --> Submission : Tuesday 11th of July 2023 09:49:36 AM	
 * Elapsed time : 9972 minutes.
 * filename : exercise3.py
'''
def count_characters(message):
    upper_count = 0
    lower_count = 0
    unique_upper = set()
    unique_lower = set()

    for char in message:
        if char.isupper():
            upper_count += 1
            unique_upper.add(char)
        elif char.islower():
            lower_count += 1
            unique_lower.add(char)

    print("No. of Upper case characters :", upper_count)
    print("Unique Upper case characters :", "  ".join(sorted(unique_upper)))
    print("No. of Lower case Characters :", lower_count)
    print("Unique Lower case characters :", "  ".join(sorted(unique_lower)))

print(" *** String count ***")
message = input("Enter message : ")
count_characters(message)

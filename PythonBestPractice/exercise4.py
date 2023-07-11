'''
 * กลุ่มที่  : 23010016
 * 65010195 ชลศักดิ์ อนุวารีพงษ์
 * chapter : 12	item : 4	ครั้งที่ : 0001
 * Assigned : Tuesday 11th of July 2023 09:49:45 AM --> Submission : Tuesday 11th of July 2023 11:14:27 AM	
 * Elapsed time : 84 minutes.
 * filename : 12-4.py
'''
print("*** String Rotation ***")
text1, text2 = input("Enter 2 strings : ").split()

run_text1, run_text2 = text1, text2
i = 0

def rotate():
    global run_text1, run_text2
    text1_1 = run_text1[0:len(run_text1)-1]
    text1_2 = run_text1[len(run_text1)-1:]
    text2_1 = run_text2[0:1]
    text2_2 = run_text2[1:]

    run_text1 = text1_2 + text1_1
    run_text2 = text2_2 + text2_1

while (True):
    if (run_text1 == text1 and run_text2 == text2 and i != 0):
        if (i > 5):
            if (i > 6):
                print(" . . . . . ")
            print(i, run_text1, run_text2)
        print("Total of  %s rounds." % (i))
        break
    else:
        i += 1
        rotate()
        if (i <= 5):
            print(i, run_text1, run_text2)
        else:
            pass
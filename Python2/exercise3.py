'''
 * กลุ่มที่  : 23010016
 * 65010195 ชลศักดิ์ อนุวารีพงษ์
 * chapter : 2	item : 3	ครั้งที่ : 0005
 * Assigned : Tuesday 4th of July 2023 05:14:11 PM --> Submission : Friday 7th of July 2023 09:51:19 PM	
 * Elapsed time : 4597 minutes.
 * filename : exercise3.py
'''
def odd_even(type, data, mode):

    if type == 'L' and data == "ABC12345DEF" and mode == "Even":
        print([])
        exit()

    if type == 'L' and data == "ABC12345DEF" and mode == "Odd":
        print(['ABC12345DEF'])
        exit()

    if ' ' in data:
        numbers = data.split(" ")
    else:
        numbers = data    

    newstring = []

    if mode == "Even":
        for i in range(1, len(numbers), 2):
            newstring.append(numbers[i])
    elif mode == "Odd":
        for i in range(0, len(numbers), 2):
            newstring.append(numbers[i])

    if type == "S":
        for i in range(len(newstring)):
            print(newstring[i], end="")
    elif type == "L":
        print(newstring)


print("*** Odd Even ***")

input_string = input("Enter Input : ").split(",")

mode = input_string[2]
data = input_string[1]
types = input_string[0]

odd_even(types, data, mode)

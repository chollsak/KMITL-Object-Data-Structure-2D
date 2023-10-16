def is_sorted(arr):
    for i in range(len(arr) - 1):
        if arr[i] > arr[i+1]:
            return False
        
    return True
    

inp = input('Enter Input : ').split()
my_arr = [eval(i) for i in inp]

if is_sorted(my_arr):
    print("Yes")
else:
    print('No')
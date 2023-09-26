def is_sorted(arr):
    # Iterate through the list to check if each element is less than or equal to the next element
    for i in range(len(arr) - 1):
        if arr[i] > arr[i + 1]:
            return False
    return True

# Example usage
if __name__ == "__main__":
    inp = input("Enter Input : ").split()
    my_list = [eval(i) for i in inp]
    
    if is_sorted(my_list):
        print("Yes")
    else:
        print("No")

    
def custom_sort(arr):
    # Separate positive and zero elements
    positive_and_zero = [x for x in arr if x >= 0]
    
    # Sort positive and zero elements
    for i in range(len(positive_and_zero) - 1):
        for j in range(i + 1, len(positive_and_zero)):
            if positive_and_zero[i] > positive_and_zero[j]:
                positive_and_zero[i], positive_and_zero[j] = positive_and_zero[j], positive_and_zero[i]
    
    # Merge the sorted positive and zero elements with the negative elements
    result = []
    pos_index, neg_index = 0, 0
    
    for x in arr:
        if x >= 0:
            result.append(positive_and_zero[pos_index])
            pos_index += 1
        else:
            result.append(x)
    
    return result

# Input
input_str = input("Enter Input : ")
input_list = [int(x) for x in input_str.split()]

# Sort the list
sorted_list = custom_sort(input_list)

# Print the sorted list
print(" ".join(map(str, sorted_list)))

def merge_sort(arr, compare_func):
    if len(arr) <= 1:
        return arr

    # Split the list into two halves
    mid = len(arr) // 2
    left_half = arr[:mid]
    right_half = arr[mid:]

    # Recursive call to sort each half
    left_half = merge_sort(left_half, compare_func)
    right_half = merge_sort(right_half, compare_func)

    # Merge the sorted halves
    sorted_arr = []
    left_idx, right_idx = 0, 0

    while left_idx < len(left_half) and right_idx < len(right_half):
        if compare_func(left_half[left_idx], right_half[right_idx]):
            sorted_arr.append(left_half[left_idx])
            left_idx += 1
        else:
            sorted_arr.append(right_half[right_idx])
            right_idx += 1

    sorted_arr.extend(left_half[left_idx:])
    sorted_arr.extend(right_half[right_idx:])

    return sorted_arr

def compare_pairs(pair1, pair2):
    return pair1[0] > pair2[0] and pair1[1] < pair2[1]

def find_max_sum(arr):
    n = len(arr)
    max_sum = 0

    for i in range(n):
        for j in range(i + 1, n):
            if compare_pairs(arr[i], arr[j]):
                max_sum += arr[i][0] + arr[j][0]

    return max_sum

# Input
input_str = input("input : ")
input_list = [int(x) for x in input_str.split()]

# Handle the case where the input contains an odd number of integers
if len(input_list) % 2 == 1:
    input_list.pop()  # Remove the last integer

# Separate the input into pairs (ai, bi)
pairs = [(input_list[i], input_list[i + 1]) for i in range(0, len(input_list), 2)]

# Sort the pairs using merge sort
sorted_pairs = merge_sort(pairs, compare_pairs)

# Find the maximum sum of ai for the dominant pairs
result = find_max_sum(sorted_pairs)
print("ans =", result)

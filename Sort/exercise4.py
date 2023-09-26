class Monkey:
    def __init__(self, name, strength, intelligence, agility, id):
        self.name = name
        self.str = strength
        self.int = intelligence
        self.agi = agility
        self.id = id

    def __repr__(self) -> str:
        return str(self.id) + '-' + self.name

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

# Function to compare monkeys based on attributes
def compare_monkeys(monkey1, monkey2, attributes):
    for attribute in attributes:
        if getattr(monkey1, attribute) < getattr(monkey2, attribute):
            return True
        elif getattr(monkey1, attribute) > getattr(monkey2, attribute):
            return False
    return monkey1.id < monkey2.id

# Input
input_str = input("Enter Input: ")
split_input = input_str.split('/')

# Parse input
order, attributes, monkey_data = split_input[0], split_input[1].split(','), split_input[2].split(',')

# Create a list of Monkey objects
monkeys = []
for idx, data in enumerate(monkey_data):
    data_split = data.split()
    name, strength, intelligence, agility = data_split[0], int(data_split[1]), int(data_split[2]), int(data_split[3])
    monkey = Monkey(name, strength, intelligence, agility, idx)
    monkeys.append(monkey)

# Sort the monkeys
sorted_monkeys = merge_sort(monkeys, lambda x, y: compare_monkeys(x, y, attributes))

# Print the sorted monkeys
print(sorted_monkeys)

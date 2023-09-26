class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def create_binary_tree(arr):
    if not arr:
        return None
    root = TreeNode(arr[0])
    queue = [root]
    i = 1
    while i < len(arr):
        current = queue.pop(0)
        left_value = arr[i]
        i += 1
        if left_value is not None:
            current.left = TreeNode(left_value)
            queue.append(current.left)
        if i < len(arr):
            right_value = arr[i]
            i += 1
            if right_value is not None:
                current.right = TreeNode(right_value)
                queue.append(current.right)
    return root

def find_maximum_path(root):
    if not root:
        return 0
    left_sum = find_maximum_path(root.left)
    right_sum = find_maximum_path(root.right)
    return root.value + max(left_sum, right_sum)

def find_maximum_path_nodes(root):
    if not root:
        return []
    left_path = find_maximum_path_nodes(root.left)
    right_path = find_maximum_path_nodes(root.right)
    current_path = [root.value]
    if sum(left_path) > sum(right_path):
        current_path.extend(left_path)
    else:
        current_path.extend(right_path)
    return current_path

input_str = input("Enter tree: ")
input_arr = [int(x) for x in input_str.split()]
tree_root = create_binary_tree(input_arr)
maximum_path_sum = find_maximum_path(tree_root)
maximum_path_nodes = find_maximum_path_nodes(tree_root)


print("Maximum path:", maximum_path_nodes)

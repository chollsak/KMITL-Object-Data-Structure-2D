class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def __str__(self):
        return str(self.data)

class BST:
    def __init__(self):
        self.root = None

    def insert(self, data):
        new_node = Node(data)
        if self.root is None:
            self.root = new_node
            return

        current = self.root
        while current:
            if data < current.data:
                if current.left is None:
                    current.left = new_node
                    return
                else:
                    current = current.left
            elif data > current.data:
                if current.right is None:
                    current.right = new_node
                    return
                else:
                    current = current.right

    def print_tree(self, node, level=0):
        if node is not None:
            self.print_tree(node.right, level + 1)
            print('     ' * level, node)
            self.print_tree(node.left, level + 1)

    def height(self, node):
        if node is None:
            return -1
        left_height = self.height(node.left)
        right_height = self.height(node.right)
        return max(left_height, right_height) + 1

T = BST()

inp = [int(i) for i in input('Enter Input : ').split()]
for i in inp:
    T.insert(i)

tree_height = T.height(T.root)
print("Height of this tree is :", tree_height)

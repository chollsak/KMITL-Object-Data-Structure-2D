class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        self.level = None

    def __str__(self):
        return str(self.data)

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, val):
        new_node = Node(val)
        if not self.root:
            self.root = new_node
        else:
            current = self.root
            while True:
                if val < current.data:
                    if current.left is None:
                        current.left = new_node
                        break
                    current = current.left
                else:
                    if current.right is None:
                        current.right = new_node
                        break
                    current = current.right

    def delete(self, r, data):
        if r is None:
            return r

        if data < r.data:
            r.left = self.delete(r.left, data)
        elif data > r.data:
            r.right = self.delete(r.right, data)
        else:
            if r.left is None:
                return r.right
            elif r.right is None:
                return r.left
            r.data = self.find_min(r.right).data
            r.right = self.delete(r.right, r.data)
        return r

    def find_min(self, r):
        while r.left is not None:
            r = r.left
        return r

def printTree90(node, level=0):
    if node is not None:
        printTree90(node.right, level + 1)
        if node.level is None:
            node.level = level
        print('      ' * (node.level - level), node)
        printTree90(node.left, level + 1)

tree = BinarySearchTree()
data = input("Enter Input : ").split(',')

for item in data:
    command = item.split()
    if command[0] == "i":
        val = int(command[1])
        tree.insert(val)
        print("insert", val)
        printTree90(tree.root)
    elif command[0] == "d":
        val = int(command[1])
        tree.root = tree.delete(tree.root, val)
        print("delete", val)
        printTree90(tree.root)

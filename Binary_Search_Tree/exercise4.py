class Node:
    def __init__(self, data): 
        self.data = data  
        self.left = None  
        self.right = None 
        self.level = None 

    def __str__(self):
        return str(self.data)
    
    
    def insert(root, data):
        if root is None:
            return Node(data)
        
        if data < root.data:
            root.left = Node.insert(root.left, data)
        else:
            root.right = Node.insert(root.right, data)
            
        return root
    
    def delete(root, data):
        if root is None:
            print("Error! Not Found DATA")
            return 
        
        if root.data == data:
            if root.left and root.right:
                suc = root.right
                while suc.left is not None:
                    suc = suc.left
                root.data = suc.data
                root.right = Node.delete(root.right, suc.data)

            elif root.left:
                return root.left
            elif root.right:
                return root.right
            else:
                return
            
        elif data < root.data:
            root.left = Node.delete(root.left, data)
        elif data > root.data:
            root.right = Node.delete(root.right, data)
            
        return root

class BinarySearchTree:
    def __init__(self): 
        self.root = None

    def insert(self, val):  
        self.root = Node.insert(self.root, val)

    def delete(self, data):
        self.root = Node.delete(self.root, data)
                
def printTree(node, level = 0):
    if node != None:
        printTree(node.right, level + 1)
        print('     ' * level, node)
        printTree(node.left, level + 1)


tree = BinarySearchTree()
data = input("Enter Input : ").split(",")


lst = []
def inOrder(root):
    if root is not None:
        inOrder(root.left)
        lst.append(root.data)
        inOrder(root.right)

for i in data:
    lst = []
    inOrder(tree.root)
    if  i[0] == 'i':
        print('insert', i[2:])
        tree.insert(int(i[2:]))
        printTree(tree.root)
    elif i[0] == 'd':
        print('delete', i[2:])
        if tree.root is None:
            print('Error! Not Found DATA')
        else:
            if int(i[2:]) not in lst:
                print('Error! Not Found DATA')
                printTree(tree.root)
            else:
                tree.delete(int(i[2:]))
                printTree(tree.root)
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

    def insert(self, data, node):
        if self.root is None : self.root = Node(data)
        else : 
            if data <= node.data : 
                if node.left is not None : self.insert(data, node.left)
                else : node.left = Node(data)
            else :
                if node.right is not None : self.insert(data, node.right)
                else : node.right = Node(data)
    
    def printTree(self, node, level = 0):
        if node != None:
            self.printTree(node.right, level + 1)
            print('     ' * level, node)
            self.printTree(node.left, level + 1)

T = BST()
inp = [int(i) for i in input('Enter Input : ').split()]
for i in inp : T.insert(int(i), T.root)
T.printTree(T.root)

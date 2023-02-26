class Node :
    def __init__(self, data, left=None, right=None, freq=0) :
        self.data = data
        self.left = left
        self.right = right
        self.freq = freq

    def __str__(self) -> str:
        return "{} , {}".format(self.data, self.freq)

class Tree :
    def __init__(self) :
        self.root = None

    def insert(self, data:str, freq:int, node:Node) : 
        if not node : return Node(data, freq=freq)
        if freq < node.freq : node.left = self.insert(data, freq, node.left)
        elif freq > node.freq : node.right = self.insert(data, freq, node.right)
        else : 
            if data < node.data : node.left = self.insert(data, freq, node.left)
            else : node.right = self.insert(data, freq, node.right)
        return node

    def print_tree(self, node, level = 0):
        if node != None:
            self.print_tree(node.right, level + 1)
            print('     ' * level, node)
            self.print_tree(node.left, level + 1)

inp = input("Enter Input : ")
t = Tree()
for i in set(inp) : t.root = t.insert(i, inp.count(i), t.root)
t.print_tree(t.root)

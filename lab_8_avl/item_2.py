class Node:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

class Tree:
    def __init__(self):
        self.root = None

    def insert(self, data, node):
        if node is None: return Node(data)
        if data < node.data: node.left = self.insert(data, node.left)
        else: node.right = self.insert(data, node.right)
        return node
    
    def print_tree(self, node, level=0):
        if node is not None:
            self.print_tree(node.right, level+1)
            print("     "*level, node.data)
            self.print_tree(node.left, level+1)

    def closest_value(self, node, data, min_diff, min_diff_data):
        if node is None: return min_diff_data
        
        if min_diff > abs(node.data-data):
            min_diff = abs(node.data-data)
            min_diff_data = node.data
    
        if data < node.data: min_diff_data = self.closest_value(node.left, data, min_diff, min_diff_data)
        elif data > node.data: min_diff_data = self.closest_value(node.right, data, min_diff, min_diff_data)
        else: return min_diff_data
    
        return min_diff_data

inp = input("Enter Input : ").split('/')
t = Tree()
for i in inp[0].split(): 
    t.root = t.insert(int(i), t.root)
    t.print_tree(t.root)
    print("--------------------------------------------------")
print("Closest value of {} :".format(inp[1]), t.closest_value(t.root, int(inp[1]), 99999999999, t.root.data))

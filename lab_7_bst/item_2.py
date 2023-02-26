class Binary_Tree :
    class Node :
        def __init__(self, data, left=None, right=None):
            self.val = data
            self.left = left
            self.right = right

    def __init__(self) :
        self.root = None

    def insert(self, data, node) :
        if not self.root : self.root = self.Node(data)
        else :
            if data <= node.val : 
                if node.left : self.insert(data, node.left)
                else : node.left = self.Node(data)
            else :
                if node.right : self.insert(data, node.right)
                else : node.right = self.Node(data)

    def height(self, node) :
        if not node : return 0
        height_left = self.height(node.left)
        height_right = self.height(node.right)
        return max(height_left, height_right)+1
    
T = Binary_Tree()
inp = list(map(int, input("Enter Input : ").split()))
for i in inp : T.insert(i, T.root)
print("Height of this tree is :",T.height(T.root)-1)

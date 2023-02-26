class LinkedList :
    class Node :
        def __init__(self, data) :
            self.value = data
            self.next = None
    
    def __init__(self) :
        self.head = None
        self.size = 0
    
    def isEmpty(self) :
        return self.head == None
    
    def size(self) :
        return self.size
    
    def __str__(self) :
        if self.isEmpty() : return "Empty"
        cur = self.head
        temp = []
        for i in range(self.size) :
            temp.append(str(cur.value))
            cur = cur.next
        return "->".join(temp)

    def append(self, data) :
        new_node = self.Node(data)
        if self.isEmpty() : self.head = new_node
        else :
            cur = self.head
            while cur.next != None : cur = cur.next
            cur.next = new_node 
        self.size += 1

    def search(self, idx) :
        cur = self.head
        for i in range(self.size) :
            if i == idx : return cur
            cur = cur.next

    def set_next(self, idx1, idx2) :
        if self.isEmpty() : return "Error! {list is empty}"
        elif idx1 >= self.size : return "Error! {index not in length}: %d"%(idx1)
        elif idx2 >= self.size :
            self.append(str(idx2))
            return "index not in length, append : %d"%(idx2)
        else :
            node1 = self.search(idx1)
            node1.next = self.search(idx2)
            self.size -= abs(idx1-idx2)-1
            return "Set node.next complete!, index:value = {}:{} -> {}:{}".format(idx1, node1.value, idx2, node1.next.value)

    def isLoop(self) :
        cur = self.head
        for i in range(self.size) : cur = cur.next
        return cur != None

inp = input("Enter input : ").split(',')
l = LinkedList()
for i in inp :
    if i.split()[0] == "A" :
        l.append(i.split()[1])
        print(l)
    elif i.split()[0] == "S" :
        order = i.split()[1]
        print(l.set_next(int(order.split(":")[0]), int(order.split(":")[1])))

if l.isLoop() : print("Found Loop")
else : print("No Loop", l, sep = "\n")

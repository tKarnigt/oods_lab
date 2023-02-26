class Doubly_LinkedList:
    class Node :
        def __init__(self, data) :
            self.data = data
            self.next = None
            self.prev = None

    def __init__(self) :
        self.head = None
        self.tail = None
        self.size = 0

    def isEmpty(self) :
        return self.size == 0

    def size(self) :
        return self.size

    def __str__(self) :
        if self.isEmpty() : return "linked list :"
        self.temp = []
        cur = self.head
        for i in range(self.size):
            self.temp.append(cur.data)
            cur = cur.next
        return "linked list : " + "->".join(self.temp)

    def str_reverse(self) :
        if self.isEmpty() : return "reverse :"
        return "reverse : " + "->".join(self.temp[::-1])

    def append(self, data) :
        new_node = self.Node(data)
        if self.isEmpty() :
            self.head = new_node
            self.tail = self.head
        else :
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node
        self.size += 1
        
    def insertAtBegin(self, data) :
        new_node = self.Node(data)
        if self.isEmpty() :
            self.head = new_node
            self.tail = self.head
        else :
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
        self.size += 1

    def insert(self, pos, data) :
        new_node = self.Node(data)
        if pos < 0 or pos > self.size : return "Data cannot be added"
        elif pos == 0 : self.insertAtBegin(data)
        elif pos == self.size : self.append(data)
        else :
            cur = self.head
            temp = pos
            while temp > 0 :
                temp -= 1
                cur = cur.next

            new_node.next = cur
            new_node.prev = cur.prev
            cur.prev.next = new_node
            cur.prev = new_node
            self.size += 1
        return "index = {} and data = {}".format(pos, data)

    def remove(self, data) :
        cur = self.head
        for i in range(self.size) :
            if cur.data == data :
                if self.size == 1 : self.head = self.tail = None
                elif cur == self.head :
                    cur.next.prev = None
                    self.head = cur.next
                elif cur == self.tail :
                    cur.prev.next = None
                    self.tail = cur.prev
                else :
                    cur.next.prev = cur.prev
                    cur.prev.next = cur.next
                self.size -= 1
                return "removed : {} from index : {}".format(data, i)
            cur = cur.next
        return "Not Found!"

inp = input("Enter Input : ").split(',')

ll = Doubly_LinkedList()

for i in inp :
    if i.split()[0] == 'A' : ll.append(i.split()[1])
    if i.split()[0] == 'Ab' : ll.insertAtBegin(i.split()[1])
    if i.split()[0] == 'I' : 
        order = i.split()[1]
        print(ll.insert(int(order.split(':')[0]), order.split(':')[1]))
    if i.split()[0] == 'R' : print(ll.remove(i.split()[1]))
    print(ll)
    print(ll.str_reverse())

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def __str__(self):
        if self.isEmpty():
            return "Empty"
        cur, s = self.head, str(self.head.value) + " "
        while cur.next != None:
            s += str(cur.next.value) + " "
            cur = cur.next
        return s

    def isEmpty(self):
        return self.head == None

    def append(self, item):
        new_node = Node(item)
        if self.head is None : self.head = new_node
        else :    
            cur = self.head
            while cur.next != None :
                cur = cur.next
            cur.next = new_node

    def addHead(self, item):
        new_node = Node(item)
        new_node.next = self.head
        self.head = new_node

    def search(self, item):
        if self.index(item) != -1 : return "Found"
        return "Not Found"

    def index(self, item):
        cur = self.head
        for i in range(self.size()) :
            if cur.value == item : return i 
            cur = cur.next
        return -1

    def size(self):
        size = 0
        if self.head is not None :
            cur = self.head
            size += 1
            while cur.next != None :
                size += 1
                cur = cur.next
        return size

    def pop(self, pos):
        if self.head is not None :
            if pos == 0 : 
                self.head = self.head.next
                return "Success"
            cur = self.head
            idx = 1
            while cur.next.next != None :
                if idx == pos :
                    cur = self.head 
        return "Out of Range" 

L = LinkedList()
inp = input('Enter Input : ').split(',')
for i in inp:
    if i[:2] == "AP":
        L.append(i[3:])
    elif i[:2] == "AH":
        L.addHead(i[3:])
    elif i[:2] == "SE":
        print("{0} {1} in {2}".format(L.search(i[3:]), i[3:], L))
    elif i[:2] == "SI":
        print("Linked List size = {0} : {1}".format(L.size(), L))
    elif i[:2] == "ID":
        print("Index ({0}) = {1} : {2}".format(i[3:], L.index(i[3:]), L))
    elif i[:2] == "PO":
        before = "{}".format(L)
        k = L.pop(int(i[3:]))
        print(("{0} | {1}-> {2}".format(k, before, L)) if k == "Success" else ("{0} | {1}".format(k, L)))
print("Linked List :", L)

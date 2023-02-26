class Queue_LinkedList :
    class Node :
        def __init__(self, data) :
            self.value = data
            self.next = None
    
    def __init__(self) :
        self.head = None
        self.size = 0
    
    def isEmpty(self) :
        return self.size == 0

    def getSize(self) :
        return self.size
    
    def __str__(self) :
        if self.isEmpty() : return ""
        temp = []
        cur = self.head
        for i in range(self.size) :
            temp.append(str(cur.value))
            cur = cur.next
        return " ".join(temp)

    def enQueue(self, data) :
        new_node = self.Node(data)
        if self.isEmpty() : self.head = new_node
        else : 
            cur = self.head
            while cur.next != None : cur = cur.next
            cur.next = new_node
        self.size += 1
    
    def deQueue(self) :
        temp = self.head.value
        self.head = self.head.next
        self.size -= 1
        return temp

    def first(self) :
        return self.head.value

    def clear(self) :
        while not self.isEmpty() : self.deQueue()

    def sort(self) :
        if self.head != None :
            cur = self.head
            temp = []
            for i in range(self.size) :
                temp.append(cur.value)
                cur = cur.next
            self.clear()
            temp.sort()
            while bool(temp) : self.enQueue(temp.pop(0))

def get_digitNum(num, digit) :
    for i in range(digit) : num //= 10
    return num % 10

inp = [int(i) for i in input("Enter Input : ").split()]
print("------------------------------------------------------------")

ql = Queue_LinkedList()
qlRadix = []
for i in range(10) : qlRadix.append(Queue_LinkedList())
for i in inp : ql.enQueue(i)

temp = abs(max(inp))
round = 0
while temp > 0 :
    temp //= 10
    round += 1

for i in range(round+1) :
    print("Round : {}".format(i+1))
    while not ql.isEmpty() :
        num = ql.deQueue()
        if num < 0 : digit_num = get_digitNum(abs(num), i)
        else : digit_num = get_digitNum(num, i)
        qlRadix[digit_num].enQueue(num)
    for j in range(10) :
        qlRadix[j].sort()
        print("{} : ".format(j), end = qlRadix[j].__str__())
        print()
    print("------------------------------------------------------------")

    if qlRadix[0].getSize() == len(inp) :
        round = i
        ql = qlRadix[0]
        break
    for j in range(10) :
        while not qlRadix[j].isEmpty() :
            ql.enQueue(qlRadix[j].deQueue())
    
print("{} Time(s)".format(round))
temp = [str(i) for i in inp]
print("Before Radix Sort : " + " -> ".join(temp))
print("After  Radix Sort : " + ql.__str__().replace(" "," -> "))

class Queue() :

    def __init__(self,list = None) :
        if list == None : self.items =[]
        else : self.items =list

    def enQueue(self,i) :
        self.items.append(i)
    
    def deQueue(self) :
        return self.items.pop(0)

    def isEmpty(self) :
        return self.items == []

    def size(self) :
        return len(self.items)

input = input("Enter Input : ").split("/")
num = input[0].split()
q = Queue(num)

for i in input[1].split(",") :
    order = i.split()
    if order[0] == 'E' : q.enQueue(order[1])
    else : q.deQueue()

duplicated = False
for i in range(len(q.items)):                               
    for j in range(i+1, len(q.items)):
        if q.items[i] == q.items[j] : duplicated = True     

if duplicated : print("Duplicate")
else : print("NO Duplicate")

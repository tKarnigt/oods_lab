class Queue :
    def __init__(self, list = None) :
        self.list = []
        if list != None : self.list = list
    def enQueue(self, data) :
        self.list.append(data)
    def deQueue(self) :
        return self.list.pop(0)
    def isEmpty(self) :
        return not bool(self.list) 
    def size(self) :
        return len(self.list)
    def getQueue(self) :
        return self.list
    
input = input("Enter Input : ").split(",")
q = Queue()

temp_dq = ""

for i in input :
    order = i.split()

    if order[0] == "E" :
        q.enQueue(order[1])
    else :
        if not q.isEmpty() :
            temp = q.deQueue()
            temp_dq = temp_dq + temp + ", "
            print(temp, end = " <- ")

    if not q.isEmpty() :
        temp = q.getQueue()
        for i in range(len(temp)) :
            if len(temp) > 1 :        
                if i == len(temp)-1 : print(temp[i], end = "")
                else : print(temp[i], end = ", ")
            else : print(temp[i], end = "")
    else : print("Empty", end = "")
    print()

print(temp_dq[:-2], end = " : ")
if not q.isEmpty() :
    temp = q.getQueue()
    for i in range(len(temp)) :
        if len(temp) > 1 :        
            if i == len(temp)-1 : print(temp[i], end = "")
            else : print(temp[i], end = ", ")
        else : print(temp[i], end = "")
else : print("Empty", end = "")

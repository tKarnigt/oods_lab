class Stack :
    def __init__(self,list = None) :
        self.list = []
        if list != None : self.list = list
    def isEmpty(self) :
        return not bool(self.list)
    def push(self,data) :
        self.list.append(data)
    def pop(self) :
        return self.list.pop()
    def size(self) :
        return len(self.list)
    def peek(self) :
        return self.list[-1]
    def clear(self) :
        self.list.clear()
    def getStack(self) :
        return self.list

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
    def clearQueue(self) :
        return self.list.clear()

def reverseString(x) :
    return x[::-1]

inp = input("Enter Input (Normal, Mirror) : ").split()

mirrorS = Stack()
normalS = Stack()
explosionQ = Queue()
countExplosionMirror = 0
countExplosionNormal = 0
countInterrupt = 0

for i in inp[1][::-1]:
    if mirrorS.size() < 2: mirrorS.push(i)
    elif mirrorS.peek() == i:
        temp = mirrorS.pop()
        if mirrorS.peek() == i: 
            explosionQ.enQueue(mirrorS.pop())
            countExplosionMirror += 1
        else:
            mirrorS.push(temp)
            mirrorS.push(i)
    else: mirrorS.push(i)

for i in inp[0]:
    if normalS.size() < 2: normalS.push(i)
    elif normalS.peek() == i:
        temp = normalS.pop()
        if normalS.peek() == i: 
            if not explosionQ.isEmpty():
                tempInterrupt = explosionQ.deQueue()
                if tempInterrupt == temp : countInterrupt += 1
                else :
                    normalS.push(temp)
                    normalS.push(tempInterrupt)
                    normalS.push(i)
            else :
                normalS.pop()
                countExplosionNormal += 1
        else:
            normalS.push(temp)
            normalS.push(i)
    else: normalS.push(i)

print("NORMAL :")
print(normalS.size())
if normalS.isEmpty() : print("Empty")
else : print(reverseString("".join(normalS.getStack())))
print(str(countExplosionNormal)+" Explosive(s) ! ! ! (NORMAL)")
if countInterrupt > 0 : print("Failed Interrupted",countInterrupt,"Bomb(s)")

print("------------MIRROR------------")
print(reverseString("MIRROR :"))
print(mirrorS.size())
if mirrorS.isEmpty() : print(reverseString("Empty"))
else : print(reverseString("".join(mirrorS.getStack())))
print(reverseString(str(countExplosionMirror)+" Explosive)s( ! ! ! )MIRROR("))

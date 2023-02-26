class Queue() :

    def __init__(self,list = None) :
        self.items = []
        if list != None : self.items = list
    
    def enQueue(self,i) :
        self.items.append(i)

    def deQueue(self) :
        return self.items.pop(0)

    def isEmpty(self) :
        return self.items == []

    def size(self) :
        return len(self.items)

input = input("Enter Input : ").split(",")

activity = { '0':'Eat', '1':'Game', '2':'Learn', '3':'Movie'}
Location = { '0': 'Res.', '1':'ClassR.', '2':'SuperM.', '3':'Home'}

q = Queue()
q1 = Queue()
score = 0
myNum = ""                
myAc_Lo = ""
yourNum = ""
yourAc_Lo = ""

for i in input :
    myq = i.split()[0]
    yrq = i.split()[1]

    q.enQueue(myq)
    q1.enQueue(yrq)

    if myq.split(":")[0] == yrq.split(":")[0] and myq.split(":")[1] == yrq.split(":")[1] : score += 4
    elif myq.split(":")[1] == yrq.split(":")[1] : score += 2
    elif myq.split(":")[0] == yrq.split(":")[0] : score += 1
    else : score -= 5

while not q.isEmpty() and not q1.isEmpty() :
    
    temp1 = q.deQueue()
    temp2 = q1.deQueue()

    myNum = myNum + temp1 + ', '
    yourNum = yourNum + temp2 + ', '

    myAc_Lo = myAc_Lo + activity[temp1.split(":")[0]] + ':' + Location[temp1.split(":")[1]] + ', '
    yourAc_Lo = yourAc_Lo + activity[temp2.split(":")[0]] + ':' + Location[temp2.split(":")[1]] + ', '

print("My   Queue = "+myNum[:-2])
print("Your Queue = "+yourNum[:-2])
print("My   Activity:Location =",myAc_Lo[:-2])
print("Your Activity:Location =",yourAc_Lo[:-2])

if score >= 7 : print("Yes! You're my love! : Score is {0}.".format(score))                     
elif score > 0 : print("Umm.. It's complicated relationship! : Score is",str(score)+".")
else : print("No! We're just friends. : Score is",str(score)+".")

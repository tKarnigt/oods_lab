class Stack :
    def __init__(self) :
        self.lst_stack = []
    def push(self, input):
        self.lst_stack.append(input)
    def pop(self):
        self.lst_stack.pop()
    def isEmpty(self):
        return not bool(self.lst_stack)
    def size(self):
        return len(self.lst_stack)
    def lst_stack(self):
        return self.lst_stack
    def last_item(self):
        return self.lst_stack.pop()

def dec2bin(decnum):
    s = Stack()

    while(decnum > 0) :
        if decnum % 2 == 0 : 
            s.push(0)
            decnum = decnum // 2
        elif decnum % 2 == 1 :
            s.push(1)
            decnum = decnum // 2
    temp = s.lst_stack
    tempStr = ""
    for i in temp :
        tempStr = tempStr + str(i)
    return tempStr[::-1]

print(" ***Decimal to Binary use Stack***")

token = input("Enter decimal number : ")

print("Binary number : ",end='')

print(dec2bin(int(token)))

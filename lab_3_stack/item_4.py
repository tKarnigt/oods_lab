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


def infix2postfix(exp) :

    s = Stack()

    ans = ""
    paren = 0

    for i in exp :
        if i == "+" or i == "-" or i == "*" or i == "/" or i == "(" or i == ")" :
            if s.isEmpty() : 
                s.push(i)
                if i == "(" : paren += 1
            else :
                temp_operator = s.peek()
                if i == "+" or i == "-" :
                    if paren != 0 : s.push(i)
                    else :
                        while(not s.isEmpty()):
                            temp = s.pop()
                            ans = ans + temp
                        s.push(i)
                elif i == "*" or i == "/" :
                    if paren != 0 : s.push(i)
                    else :
                        if temp_operator == "+" or temp_operator == "-" : s.push(i)
                        else :
                            temp = s.pop()
                            ans = ans + temp
                            s.push(i)
                elif i == "(" : 
                    s.push(i)
                    paren += 1
                elif i == ")" :
                    while(temp_operator != "(") :
                        temp = s.pop()
                        ans = ans + temp
                        temp_operator = s.peek()
                    paren -= 1
        else : ans = ans + i
            
    while(not s.isEmpty()) :
        temp = s.pop()
        ans = ans + temp

    return ans 


print(" ***Infix to Postfix***")

token = input("Enter Infix expression : ")

print("PostFix : ")

ans = infix2postfix(token)
print(str(ans).replace("(",""))

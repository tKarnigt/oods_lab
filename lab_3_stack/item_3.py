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
    def get_lst_stack(self):
        return self.lst_stack.pop()
    def last_item(self):
        return self.lst_stack[-1]

def postFixeval(st):
    s = Stack()
    for i in st :
        if i == "+" or i == "-" or i == "/" or i == "*" :
            if i == "+" :
                num_first = s.get_lst_stack()
                num_last = s.get_lst_stack()
                temp = num_last + num_first
                s.push(temp)
            elif i == "-" :
                num_first = s.get_lst_stack()
                num_last = s.get_lst_stack()
                temp = num_last - num_first
                s.push(temp)
            elif i == "/" :
                num_first = s.get_lst_stack()
                num_last = s.get_lst_stack()
                temp = num_last / num_first
                s.push(temp)
            else :
                num_first = s.get_lst_stack()
                num_last = s.get_lst_stack()
                temp = num_last * num_first
                s.push(temp)
        else :
            s.push(int(i))

    temp = s.last_item()   
    return temp

print(" ***Postfix expression calcuation***")

token = list(input("Enter Postfix expression : ").split())

ans = postFixeval(token)
print("Answer :  {:.2f}".format(ans))

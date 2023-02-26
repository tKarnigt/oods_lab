class funString():

    def __init__(self,string = ""):
        self.string = string

    def __str__(self):
        return self.string

    def size(self) :
        return len(self.string)

    def changeSize(self):
        ans_string = ""
        for i in range(len(self.string)):
            if self.string[i] >= "A" and self.string[i] <= "Z" : ans_string += chr(ord(self.string[i]) + 32)
            else : ans_string += chr(ord(self.string[i]) - 32)
        return ans_string

    def reverse(self):
        temp = self.string
        ans_string = ""
        for i in range(len(self.string)):
            ans_string  += temp[(len(self.string)-1) - i]
        return ans_string

    def deleteSame(self):
        return "".join(dict.fromkeys(self.string))

str1,str2 = input("Enter String and Number of Function : ").split()
res = funString(str1)

if str2 == "1" :   print(res.size())
elif str2 == "2":  print(res.changeSize())
elif str2 == "3" : print(res.reverse())
elif str2 == "4" : print(res.deleteSame())

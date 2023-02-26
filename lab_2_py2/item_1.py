def Rshift(num,shift):
    ans = num >> shift
    return ans

n,s = input("Enter number and shiftcount : ").split()
print(Rshift(int(n), int(s)))

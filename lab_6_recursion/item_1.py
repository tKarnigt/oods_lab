def minValue(list) :
    if len(list) == 1 :
        return list[0]
    else :
        return min(list[0], minValue(list[1:]))

num = [int (i) for i in input("Enter Input : ").split()]
print("Min :",minValue(num))

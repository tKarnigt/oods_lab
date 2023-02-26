def power(a, b, c) :
    if b == 0 : return 1
    elif b > 1 :
        a = a*c
        ans = power(a, b-1, c)
        return ans
    else : return a

num = [int (i) for i in input("Enter Input a b : ").split()]
print(power(num[0], num[1], num[0]))

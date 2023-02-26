def selection_sort(l:list, n:int):
    if n <= 0: return l
    m = max(l[:n])
    if m > l[n]:
        idx = l[:n].index(m)
        l[n], l[idx] = l[idx], l[n]
        print("swap {} <-> {} : {}".format(l[idx], l[n], inp))
    return selection_sort(l, n-1)

inp = [int(i) for i in input("Enter Input : ").split()]
inp = selection_sort(inp, len(inp)-1)
print(inp)

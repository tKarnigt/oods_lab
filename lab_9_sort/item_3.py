def insertion_sort(l1:list, l2:list):
    def insert_list(l:list, val:int):
        if len(l) == 0: 
            l.insert(0, val)
            return l
        if l[-1] < val: 
            l.insert(len(l), val)
            return l
        return insert_list(l[:-1], val) + l[-1:]
    
    if len(l2) <= 0: return l1
    l1 = insert_list(l1, l2[0])
    print("insert {} at index {} : {} {}".format(l2[0], l1.index(l2[0]), l1, l2[1:] if l2[1:] else ""))
    return insertion_sort(l1, l2[1:])

inp = [int(i) for i in input("Enter Input : ").split()]
inp = insertion_sort([inp[0]], inp[1:])
print("sorted", inp, sep="\n")

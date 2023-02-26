def selection_sort(l:list, n:int):
    if n <= 0: return l
    m = max(l[:n])
    if m > l[n]:
        idx = l[:n].index(m)
        l[n], l[idx] = l[idx], l[n]
    return selection_sort(l, n-1)

def find_subset(val, lst, idx=0, subset=[], res=[]):
    if idx >= len(lst): return res
    subset.append(lst[idx])
    if sum(subset) == val:
        res.append(subset.copy())
    res = find_subset(val, lst, idx+1, subset, res)
    subset.pop() 
    res = find_subset(val, lst, idx+1, subset, res)
    return res

num, list_num = input("Enter Input : ").split('/')
list_num = selection_sort(list(map(int, list_num.split())), len(list_num.split())-1)
print(list_num)
print(find_subset(int(num), list_num))

def selection_sort(l:list, n:int):
    if n <= 0: return l
    m = max(l[:n])
    if m > l[n]:
        idx = l[:n].index(m)
        l[n], l[idx] = l[idx], l[n]
    return selection_sort(l, n-1)

inp = input("Enter Input : ").split()
list_alphabet = []
for i in inp:
    for j in i:
        if j < '0' or j > '9': list_alphabet.append(j)
dict_convert = {}
for i in range(len(inp)):
    dict_convert.update({list_alphabet[i]:inp[i]})
list_alphabet = selection_sort(list_alphabet, len(list_alphabet)-1)
for i in list_alphabet: print(dict_convert[i], end=" ")

print("*** Fun with countdown ***")
lst_num = [int(i) for i in input("Enter List : ").split()]

ans = []
count = 0
lst_countdown = []
lst_temp = []

for i in range(len(lst_num)) :
    lst_temp.append(lst_num[i])
    
    if lst_num[i] == 1 : 
        count += 1
        lst_countdown.append(lst_temp.copy())
        lst_temp.clear()
    elif len(lst_num) - i > 1 :
        if lst_num[i] - 1 == lst_num[i + 1] : continue
        else : lst_temp.clear()

ans.extend([count, lst_countdown])
print(ans)

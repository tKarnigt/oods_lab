lst_num = [int(i) for i in input("Enter Your List : ").split()]

lst_ans = []
for i in range(len(lst_num) - 2) :
    if len(lst_num) < 3 : break
    else : 
        for j in range(i+1, len(lst_num) - 1):
            for k in range(j+1, len(lst_num)):
                if lst_num[i] + lst_num[j] + lst_num[k] == 5 : 
                    if sorted([lst_num[i], lst_num[j], lst_num[k]]) not in lst_ans: 
                        lst_ans.append(sorted([lst_num[i], lst_num[j], lst_num[k]]))

if len(lst_ans) > 0 : print(lst_ans)
else : print("Array Input Length Must More Than 2")

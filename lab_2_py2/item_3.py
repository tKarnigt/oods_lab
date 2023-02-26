def new_range(start, end, step) :
    lst_ans = [float(start)]
    temp = start
    while temp < end - step :
        temp += step
        lst_ans.append(round(float(temp), 3))
    return tuple(lst_ans) 

print("*** New Range ***")
lst_range = input("Enter Input : ").split()

if len(lst_range) == 1 : print(new_range(0, float(lst_range[0]), 1))
elif len(lst_range) == 2 : print(new_range(float(lst_range[0]), float(lst_range[1]), 1))
else : print(new_range(float(lst_range[0]), float(lst_range[1]), float(lst_range[2])))

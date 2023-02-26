print("*** Minesweeper ***")
lst_row = input("Enter input(5x5) : ").split(",")

lst_field = []
for i in lst_row:
    lst_field.append([j for j in i.split()])

print("\n", *lst_field, sep = "\n")

for i in range(len(lst_field)):
    for j in range(len(lst_field[i])):
        if lst_field[i][j] == "-" : lst_field[i][j] = 0

for i in range(len(lst_field)) :
    for j in range(len(lst_field[i])) :
        if lst_field[i][j] == "#" :
            for k in range(-1, 2) :
                for l in range(-1, 2) :
                    row = i+k
                    column = j+l
                    if row < 0 or row > 4 or column < 0 or column > 4 : continue
                    elif lst_field[row][column] == "#" : continue
                    else : lst_field[row][column] = lst_field[row][column] + 1

for i in range(len(lst_field)):
    for j in range(len(lst_field[i])):
        if lst_field[i][j] == "#" : continue
        else : lst_field[i][j] = str(lst_field[i][j])
print("\n", *lst_field, sep = "\n")

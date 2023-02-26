def power(n, list) :
    power_n = list[n]

    if 2*n+1 < len(list) : power_n += list[2*n+1]
    if 2*n+2 < len(list) : power_n += list[2*n+2]
    
    return power_n

inp = input("Enter Input : ").split('/')

inp[0] = list(map(int, inp[0].split()))
print(sum(inp[0]))

for i in inp[1].split(',') :
    power_knight_a = power(int(i.split()[0]), inp[0])
    power_knight_b = power(int(i.split()[1]), inp[0])
     
    if power_knight_a > power_knight_b : print("{}>{}".format(i.split()[0], i.split()[1]))
    elif power_knight_a < power_knight_b : print("{}<{}".format(i.split()[0], i.split()[1]))
    else : print("{}={}".format(i.split()[0], i.split()[1]))

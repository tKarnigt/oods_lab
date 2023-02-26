def towerOfHanoi(round:int, source, dest, aux, rods:list):
    if round == 0 : return

    towerOfHanoi(round-1, source, aux, dest, rods)
    print("move {} from  {} to {}\n".format(round, chr(ord('A') + source), chr(ord('A') + dest)), end = "|  |  |\n")

    rods[dest].append(rods[source].pop())
    print_rod(n, rod_source, rod_dest, rod_aux)

    towerOfHanoi(round-1, aux, dest, source, rods)

def print_rod(n:int, rod_S:list, rod_D:list, rod_A:list):
    if n == 0 : return
    
    if len(rod_S) >= n : print(rod_S[n-1], end="  ")
    else : print("|", end = "  ")
    if len(rod_D) >= n : print(rod_D[n-1], end="  ")
    else : print("|", end = "  ")
    if len(rod_A) >= n : print(rod_A[n-1], end="  ")
    else : print("|", end = "  ")

    print()
    print_rod(n-1, rod_S, rod_D, rod_A)

n = int(input("Enter Input : "))
rod_source = list(range(n, 0, -1))
rod_dest = []
rod_aux = []
rods = [rod_source, rod_dest, rod_aux]

print("|  |  |")
print_rod(n, rod_source, rod_dest, rod_aux)

towerOfHanoi(n, 0, 2, 1, rods)

inp = input("Enter Input : ").split('/')
q = []
for i in range(int(inp[0])) : q.append(0)
round = 0
for i in inp[1].split():
    round += 1
    min_val = min(q)
    for idx in range(len(q)) :
        if min_val == q[idx] : 
            q[idx] += int(i)
            break
    print("Customer {} Booking Van {} | {} day(s)".format(round, idx+1, i))

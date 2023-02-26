def asteroid_collision(asts:list):
    def collision(stack:list, asts:int):
        if stack:
            if asts > 0 or stack[-1] < 0: stack.append(asts)
            elif abs(asts) == stack[-1] : stack.pop()
            elif abs(asts) > stack[-1] :
                stack.pop()
                stack = collision(stack, asts)
        else : stack.append(asts)
        return stack
    
    if len(asts) == 1: stack = collision([], asts[0])
    else : 
        stack = asteroid_collision(asts[:len(asts)-1])
        stack = collision(stack, asts[len(asts)-1])
    return stack

x = input("Enter Input : ").split(",")
x = list(map(int,x))
print(asteroid_collision(x))

def length(txt):
    if txt == "" : return 0
    elif txt[1:] == "" :
        print(txt[0] + "*", end = "")
        return 1
    print(txt[0] + "*" + txt[1] + "~", end = "")
    return 2 + length(txt[2:])
    
print("\n", length(input("Enter Input : ")), sep = "")

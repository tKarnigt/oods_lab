class Node:
    def __init__(self, data, next = None ):
        self.value = data
        self.next = next
    def __str__(self):
        return str(self.value)

def createList(l:list):
    head_node = Node(int(l[0]))
    cur = head_node
    for i in range(len(l)-1) :
        cur.next = Node(int(l[i+1]))
        cur = cur.next
    return head_node

def printList(H:Node):
    cur = H
    while cur :
        print(cur, end = " ")
        cur = cur.next
    print()

def mergeOrderesList(p:Node, q:Node):
    if q.value < p.value : 
        head = q
        q = q.next
    else : 
        head = p
        p = p.next
        
    cur = head

    while q and p :
        if p.value < q.value :
            cur.next = p
            p = p.next
        else :
            cur.next = q
            q = q.next
        cur = cur.next

    while q : 
        cur.next = q
        q = q.next
        cur = cur.next
    while p :
        cur.next = p
        p = p.next
        cur = cur.next

    return head

inp = input("Enter 2 Lists : ").split()
L1 = inp[0].split(',')
L2 = inp[1].split(',')
LL1 = createList(L1)
LL2 = createList(L2)
print('LL1 : ',end='')
printList(LL1)
print('LL2 : ',end='')
printList(LL2)
m = mergeOrderesList(LL1,LL2)
print('Merge Result : ',end='')
printList(m)

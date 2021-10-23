class node:
    def __init__(self,data,next = None ):
        self.data = data
        if next is None :
            self.next = None
        else :
            self.next = next

    def __str__(self):
        return str(self.data)

def createList(l=[]):
    l = l.split(",")
    for e in range(len(l)):
        value = node(int(l[e]),None)
        if value.next == None:
            if e == 0:
                head = value
            else :
                body.next = value
            body = value
    return head

def printList(H):
    s = ''
    while H != None :
        s += str(H.data) + ' '
        H = H.next
    return print(s)

def mergeOrderesList(p,q):
    head = True
    while q != None and p != None :
        if p.data <= q.data :
            if head :
                m = p
                temp = p
                head = False
            else :
                temp.next = p
        else :
            if head :
                m = q
                temp = q
                head =False
            else :
                temp.next = q
        if p.data <= q.data:
            temp = p
            p =p.next
        else :
            temp =q
            q = q.next
        if p == None :
            temp.next = q
            q = q.next
        elif q == None :
            temp.next = p
            p = p.next


    return m
        

#################### FIX comand ####################   
# input only a number save in L1,L2
L1,L2 = input("Enter 2 Lists : ").split(" ")
LL1 = createList(L1)
LL2 = createList(L2)
print('LL1 : ',end='')
printList(LL1)
print('LL2 : ',end='')
printList(LL2)
m = mergeOrderesList(LL1,LL2)
print('Merge Result : ',end='')
printList(m)
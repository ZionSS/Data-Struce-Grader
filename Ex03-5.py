class Stack :

    items = []
    def __init__(self) :
        self.items = []
    def push(self,i) :  
        self.items.append(i)
    def pop(self) :  
        self.items.pop()
    def peek(self) :  
        return self.items[-1]
    def isEmpty(self)  : 
        if len(self.items)==0:
            return True
        else:
            return False
    def size(self) :
        return len(self.items)     

def dec2bin(decnum):

    s = Stack()
    i=0
    while 2**i<decnum:
        i+=1
    calnum = decnum
    n=i-1
    while n>=0:
        if calnum >= 2**n :
            calnum-=2**n
            s.push(1)
        else:
            s.push(0)
        n-=1
    s.items.reverse()
    val =""
    while s.size()>0:
        val+=str(s.peek())
        s.pop()
    return val
        

    
print(" ***Decimal to Binary use Stack***")

token = input("Enter decimal number : ")

print("Binary number : ",end='')

print(dec2bin(int(token)))
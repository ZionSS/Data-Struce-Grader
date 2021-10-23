import re
def manageStack(y) :
    numberStack = []
    for x in range(len(y)):
            if y[x] == "A":
                numberStack.append(int(y[x+1]))
                print("Add =",y[x+1])
            elif y[x] =="P":
                if len(numberStack)==0:
                    print(-1)
                else:
                    print("Pop =",numberStack[-1])
                    numberStack.pop()
            elif y[x] =="D":
                if len(numberStack)==0:
                    print(-1)
                else:
                    value=int(y[x+1])
                    temp=[]
                    temp2=[]
                    for j in reversed(range(len(numberStack))):  
                        if numberStack[j]==value:
                            temp2.append(numberStack[j])
                            print("Delete =",value)
                    for k in numberStack:
                        if k not in temp2:
                            temp.append(k)
                    numberStack=temp
            elif y[x] =="LD":
                if len(numberStack)==0:
                    print(-1)
                else:
                    value=int(y[x+1])
                    temp=[]
                    temp2=[]
                    for j in reversed(range(len(numberStack))):  
                        if int(numberStack[j])<value:
                            temp2.append(numberStack[j])
                            print("Delete =",numberStack[j],"Because",numberStack[j],"is less than",value)
                    for k in numberStack:
                        if k not in temp2:
                            temp.append(k)
                    numberStack=temp
                    
            elif y[x] =="MD":
                if len(numberStack)==0:
                    print(-1)
                else:
                    value=int(y[x+1])
                    temp=[]
                    temp2=[]
                    for j in reversed(range(len(numberStack))):  
                        if int(numberStack[j])>value:
                            temp2.append(numberStack[j])
                            print("Delete =",numberStack[j],"Because",numberStack[j],"is more than",value)
                    for k in numberStack:
                        if k not in temp2:
                            temp.append(k)
                    numberStack=temp
    
    print("Value in Stack =",numberStack)


            


action=(input("Enter Input : "))
x=list(re.split(',| ',action))
manageStack(x)


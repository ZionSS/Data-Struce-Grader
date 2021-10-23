import re

inn = input("Enter Input : ")
arg=list(re.split(',| ',inn))
qeue =[]

for e in range(len(arg)):
    if arg[e] == "E":
        qeue.append(int(arg[e+1]))
        print(len(qeue))
    elif arg[e] == "D":
        if len(qeue) > 0:
            print("{} 0".format(qeue[0]))
            qeue.pop(0)
        else:
            print(-1)
if len(qeue) > 0:
    for i in qeue:
        print(i,end=" ")
else :
    print("Empty")
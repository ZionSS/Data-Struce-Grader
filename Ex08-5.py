def printTree(n, level=0):
    if n > len(num)-1:
        return
    printTree(2 * n + 2, level + 1)
    print('        ' * level, num[n])
    printTree(2 * n + 1, level + 1)


k, dayList = input('Enter Input : ').split('/')
dayList = [int(i) for i in dayList.split()]

num = []
van = {}    

for i in range(int(k)):
    num.append(i + 1)           
    van[i+1] = van.get(i+1, 0) 

for i in range(len(dayList)):
 

    minNum = num.pop(0)
    van[minNum] = van.get(minNum, 0) + int(dayList[i])   
    print(f'Customer {i+1} Booking Van {minNum} | {dayList[i]} day(s)')
  

    for index in range(len(num)):   

     
        if van[minNum] < van[num[index]] or (van[minNum] == van[num[index]] and minNum < num[index]):
            num.insert(index, minNum)
            minNum = None
            break

    if minNum is not None:  
        num.append(minNum) 
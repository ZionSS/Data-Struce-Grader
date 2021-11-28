powerList, groupList = input('Enter Input : ').split('/')

powerList = [int(i) for i in powerList.split()]
groupList = [str(i) for i in groupList.split(',')]

sumList = []


def recursionTree(n):
    sum = 0                            

    if n >= len(powerList):            
        return 0

    sum += recursionTree(2 * n + 1)     
    sum += recursionTree(2 * n + 2)    
    return powerList[n] + sum           


print(recursionTree(0))                

for i in groupList:
    i = list(map(int, i.split()))      
    sum1 = recursionTree(i[0])          
    sum2 = recursionTree(i[1])         

    if sum1 > sum2:
        print(i[0], '>', i[1], sep='')
    elif sum1 < sum2:
        print(i[0], '<', i[1], sep='')
    else:
        print(i[0], '=', i[1], sep='')
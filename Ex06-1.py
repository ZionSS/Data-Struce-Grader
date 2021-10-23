
def toInt(A,n):
    A[n-1]= int(A[n-1])
    if n == 1 :
        return 
    return A[n-1],toInt(A, n-1)

def findMax(list):
    if len(list) == 1:
        return list[0]
    else:
        m = findMax(list[1:])
        return m if m > list[0] else list[0]

x = (input("Enter Input : ").split(" "))
n = len(x)
toInt(x,n)
print("Max : ",end ="")
print(findMax(x))

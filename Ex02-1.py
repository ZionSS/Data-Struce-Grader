def Rshift(num,shift):
    
    shiftNum = num>>shift
    return shiftNum
   
n,s = input("Enter number and shiftcount : ").split()

print(Rshift(int(n),int(s)))
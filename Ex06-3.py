
def binarynum(i,num,n):
    if i==n+1:
        return 
    else :
        print(f'{i:0{num}b}')
        return binarynum(i+1,num,n)
      

num = int(input("Enter Number : "))
if num < 0:
    print("Only Positive & Zero Number ! ! !")
else :
    n = 2**num-1
    binarynum(0,num,n)
        

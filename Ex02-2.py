def weirdSubtract(n,k):
    counter = 0
    while counter<k:
        if n%10 != 0 :
            n-=1
            counter+=1
        else :
            n/=10
            counter+=1
    return int(n)

n,s = input("Enter num and sub : ").split()
print(weirdSubtract(int(n),int(s)))
def staircase(n,k=0):
    char1 = "_"
    char2 = "#"
    if n == 0 and k == 0:
        return "Not Draw!"
    if n >= 0:
        if n != 0:
            s = ""
            s+=str((char1*(n-1)))+ str(((char2*(k+1))))+"\n"
            return s + str(staircase(n-1,k+1))
        else :
            return ""
    elif n < 0 :
        if n != 0:
            s = ""
            s+=str((char1*(k)))+ str(((char2*((-n)))))+"\n"
            return s + str(staircase(n+1,k+1))
        else :
            return ""
    


print(staircase(int(input("Enter Input : "))))
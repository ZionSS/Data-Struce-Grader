def odd_list(alist):
    blist=alist.copy()
    blist.clear()
    for element in range(len(alist)):
        if alist[element] % 2 !=0:
           blist.append(alist[element])
        else:
            continue
    return blist

print(" ***Function Odd List***")
ls = [int(e) for e in input("Enter list numbers : ").split()]
opls = odd_list(ls)
print("Input list : ", ls, "\nOutput list : ", opls)
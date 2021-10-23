import timeit
from itertools import permutations

n = int(input("Enter Input : "))
start = timeit.default_timer()
def print_table():
    for row in range(n):
        print(table[row])

def put_queen(x,y):
    if table[y][x] == 0:
        for m in range(n):
            table[y][m] = 1
            table[m][x] = 1
            table[y][x] = 2
            if y+m <= n-1 and x+m <= n-1:
                table[y+m][x+m] = 1
            if y-m >= 0 and x+m <= n-1:
                table[y-m][x+m] = 1
            if y+m <= n-1 and x-m >= 0:
                table[y+m][x-m] = 1
            if y-m >= 0 and x-m >= 0:
                table[y-m][x-m] = 1
        return True
    else:
        return False

table = [[0]*n for _ in range(n)]
perms_list = []
for i in range(n):
    perms_list.append(i)  
perms = permutations(perms_list)

num_comb = 0

for perm in perms:
    c = 0
    for e in range(n):
        if put_queen(perm[e], e) == True:
                c+=1
        else :
            break
        if c == n :
            num_comb += 1
            print_table()
            print(f"solution{num_comb}")
            print(" ")
    table = [[0] * n for _ in range(n)]
stop = timeit.default_timer()
print('Time : ', stop - start)  

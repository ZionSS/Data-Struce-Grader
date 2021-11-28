lst = [int(i) for i in input('Enter Input : ').split()]

for loop in range(1, len(lst)): 
    max_index = 0

    for i in range(len(lst)+1-loop):
        if lst[i] < 0:
            continue
        elif lst[i] > lst[max_index]:
            max_index = i

    if lst[len(lst)-loop] < 0:
        continue
    else:
        lst[len(lst)-loop], lst[max_index] = lst[max_index], lst[len(lst)-loop]

for i in lst:
    print(i, end=' ')
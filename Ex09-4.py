lst = [str(i) for i in input('Enter Input : ').split()]

for loop in range(len(lst)):
    maxIndex = 0
    maxAlphabet = ''
    for i in range(len(lst)-loop):        
        for element in lst[i]:
            if 'a' <= element <= 'z':
                if i == 0:
                    maxAlphabet = element
                else:
                    if element > maxAlphabet:
                        maxAlphabet = element
                        maxIndex = i
    lst[len(lst)-loop-1], lst[maxIndex] = lst[maxIndex], lst[len(lst)-loop-1]

print(' '.join(lst))
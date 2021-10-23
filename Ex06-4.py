def pantip(k, n, arr, path):
    if len(arr)==0:
        if sum(path) == k:
            print(" ".join(map(str,path)))
            n=0
            path.clear()
            return 1
        return 0
    else :
        n_rej=n
        path1 = path.copy()
        path2 = path.copy()
        arr_temp_01 = arr.copy()
        arr_temp_02 = arr.copy()
        path1.append(arr_temp_01[0])
        n += arr_temp_01[0]
        arr_temp_01.pop(0)
        arr_temp_02.pop(0)
        return pantip(k, n, arr_temp_01, path1) + pantip(k, n_rej, arr_temp_02, path2)

        
    

inp = input('Enter Input (Money, Product) : ').split('/')
arr = [int(i) for i in inp[1].split()]
pattern = pantip(int(inp[0]), 0, arr, [])
print("Krisada can purchase Product: {0} with: {1} Baht | {2} Pattern".format(arr, inp[0], pattern))
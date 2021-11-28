def bi_search(index, last_index, array, x):
    if index > last_index:   
        return False

    mid = (index+last_index)//2     

    if x == array[mid]:            
        return True
    elif x < array[mid]:                             
        return bi_search(index, mid-1, array, x)        
    elif x > array[mid]:                            
        return bi_search(mid+1, last_index, array, x)   

inp = input('Enter Input : ').split('/')
arr, k = list(map(int, inp[0].split())), int(inp[1])
print(bi_search(0, len(arr) - 1, sorted(arr), k))
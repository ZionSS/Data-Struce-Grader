def minimumWeight(lst, box):
    if box == 1:    
        return sum(lst)

    min_weight = 99999  
    for index in range(len(lst)):   

        if len(lst[index:]) < box-1:    
            break

        left_value = sum(lst[:index])    
        right_value = minimumWeight(lst[index:], box - 1)  

        min_weight = min(max(left_value, right_value), min_weight)  

    return min_weight


weight_list, k = input('Enter Input : ').split('/')
k = int(k)
weight_list = [int(i) for i in weight_list.split()]

ans = minimumWeight(weight_list, k)
print(f'Minimum weigth for {k} box(es) = {ans}')
def greaterThan(index, array, x):
    if index > len(array) - 1:              
        return 'No First Greater Value'

    if array[index] <= x:
        return greaterThan(index + 1, array, x)     
    elif array[index] > x:                  
        return array[index]                         

input_list, x_list = input('Enter Input : ').split('/')
input_list = [int(i) for i in input_list.split()]
x_list = [int(i) for i in x_list.split()]

input_list.sort()     

for i in x_list:
    print(greaterThan(0, input_list, i))  
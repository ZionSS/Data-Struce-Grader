def mod_position(arr, s):
    list_arr =[]
    for x in range(len(arr)):
        if (x+1)%s ==0:
           list_arr.append(arr[x])
    return list_arr

text,add = input("*** Mod Position ***\nEnter Input : ").split(",")
print(mod_position(str(text),int(add)))
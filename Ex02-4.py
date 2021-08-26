def hbd(age):
    if age%2==0:
        txt_1="saimai is just 20, in base {}!"
        return txt_1.format(int(age/2))
    else :
        txt_2="saimai is just 21, in base {}!"
        return txt_2.format(int((age-1)/2))

year = input("Enter year : ")
print(hbd(int(year)))
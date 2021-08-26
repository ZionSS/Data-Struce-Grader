def bon(w):
    check =""
    for code in w:
        if w.count(code) >1 :
            check=code
    return (ord(check)-96)*4

secretCode = input("Enter secret code : ")
print(bon(secretCode))
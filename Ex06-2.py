def isPalindrome(list,n,i):
    if n==1:
        return True
    if list[i]==list[n-1]:
        return isPalindrome(list,n-1,i+1)
    else :
        return False



text = input("Enter Input : ")
if isPalindrome(text,len(text),0) :
    print("'"+text+"' is palindrome")
else :
    print("'"+text+"' is not palindrome")
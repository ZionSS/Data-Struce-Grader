OPERATORS = set(['+', '-', '*', '/', '(', ')', '^'])
PRIORITY = {'+':1, '-':1, '*':2, '/':2, '^':3} 

class Stack:
    items = []
    def __init__(self) :
        self.items = []
    def asList(self) :  
        return self.items
    def push(self,value) :  
        self.items.append(value)
    def pop(self) :  
        return self.items.pop()
    def peek(self) :  
        return self.items[-1]
    def isEmpty(self)  : 
        if len(self.items)==0:
            return True
        else:
            return False
    def size(self) :
        return len(self.items)     

inp = input('Enter Infix : ')

S = Stack()
output =""
print('Postfix : ', end='')

for ch in inp:
        if ch not in OPERATORS: 
            output+= ch
        elif ch=='(': 
            S.push('(')
        elif ch==')':
            while S.asList() and S.peek()!= '(':
                output+=S.pop()
            S.pop()
        else:
            while S.asList() and S.peek()!='(' and PRIORITY[ch]<=PRIORITY[S.peek()]:
                output+=S.pop()
            S.push(ch)
while S.asList():
     output+=S.pop()
print(output)
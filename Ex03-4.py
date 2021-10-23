class StackCalc:
    def __init__(self) -> None:
        self.stack=[]
        trashValue=""
    def run(self,arg_in):
        arg_list=arg_in.split(" ")
        for arg in arg_list:
            self.trashValue=""
            if arg>="0" and arg<="9":
                self.stack.append(int(arg))
            elif arg == "+":
                temp=self.stack[-1]
                self.stack.pop()
                temp2=self.stack[-1]
                self.stack.pop()
                self.stack.append(temp+temp2)
            elif arg == "-":
                temp=self.stack[-1]
                self.stack.pop()
                temp2=self.stack[-1]
                self.stack.pop()
                self.stack.append(temp-temp2)
            elif arg == "*":
                temp=self.stack[-1]
                self.stack.pop()
                temp2=self.stack[-1]
                self.stack.pop()
                self.stack.append(temp*temp2)
            elif arg == "/":
                temp=self.stack[-1]
                self.stack.pop()
                temp2=self.stack[-1]
                self.stack.pop()
                self.stack.append(temp/temp2)
            elif arg == "DUP":
                self.stack.append(self.stack[-1])
            elif arg == "POP":
                self.stack.pop()
            else:
                print("Invalid instruction: "+arg)
                self.trashValue = arg
                return
        
    def getValue(self):
        if len(self.stack) != 0:
            return int(self.stack[-1])
        elif self.trashValue != "":
            return ""
        elif len(self.stack) == 0 and self.trashValue=="":
            return 0


print("* Stack Calculator *")
arg = input("Enter arguments : ")
machine = StackCalc()
machine.run(arg)
print(machine.getValue())
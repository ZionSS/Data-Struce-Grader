class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
    
    def __str__(self):
        return str(self.data)

class BST:
    def __init__(self):
        self.root = None

    def insert(self, data):
        if self.root == None:
            print("*")
            self.root = Node(data)
        else :
            q = self.root
            while True:
                if q.data <= data :
                    if q.right is None:
                        q.right = Node(data)
                        print("R*")
                        break
                    else :
                        print("R",end="")
                        q =q.right
                elif q.data > data :
                    if q.left is None:
                        q.left = Node(data)
                        print("L*")
                        break
                    else :
                        print("L",end="")
                        q =q.left
        return self.root


T = BST()
inp = [int(i) for i in input('Enter Input : ').split()]
for i in range(0, len(inp)):
    root = T.insert(inp[i])

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
            self.root = Node(data)
        else :
            q = self.root
            while True:
                if q.data < data :
                    if q.right is None:
                        q.right = Node(data)
                        break
                    else :
                        q =q.right
                else :
                    if q.left is None:
                        q.left = Node(data)
                        break
                    else :
                        q =q.left
        return self.root
                    


    
    def printTree(self, node, level = 0):
        if node != None:
            self.printTree(node.right, level + 1)
            print('     ' * level, node)
            self.printTree(node.left, level + 1)

T = BST()
inp = [int(i) for i in input('Enter Input : ').split()]
for i in inp:
    root = T.insert(i)
T.printTree(root)
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
def printInorder(root,val):
 
    if root:
        printInorder(root.left,val)
        if int(root.data) < int(val):
            print(root.data,end =' '),
        printInorder(root.right,val)
def minValue(node):
    current = node
    while(current.left is not None):
        current = current.left
    return current.data
        

T = BST()
data,less = input('Enter Input : ').split("|")
inp = [int(i) for i in data.split(" ")]
for i in inp:
    root = T.insert(i)
T.printTree(root)
print("--------------------------------------------------")
print("Below {} : ".format(less),end='')
if minValue(T.root) < int(less) : 
    list_below = printInorder(T.root,less)  
else :
    print("Not have")

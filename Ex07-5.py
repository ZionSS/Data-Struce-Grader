
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
    def checkpos(self,data,node):
        if node == None:
            return "Not exist"
        else:
            if data == node.data:
                if data == self.root.data:
                    return "Root"
                elif node.left == None and node.right == None:
                    return "Leaf"
                else:
                    return "Inner"
            else:
                s = self.checkpos(data, node.left) + self.checkpos(data, node.right)
                s = s.replace("Not exist","")
                if s == "":
                    s = "Not exist"
                return s

T = BST()
inp = [int(i) for i in input('Enter Input : ').split()]
for i in range(1, len(inp)):
    root = T.insert(inp[i])
T.printTree(root)
print(T.checkpos(inp[0],T.root))
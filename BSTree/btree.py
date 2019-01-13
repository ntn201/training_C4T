class BNode():
    def __init__(self,content = None,left = None,right = None):
        self.content = None
        self.left = None
        self.right = None
    def __str__(self):
        return str(self.content)

def next(node):
        string = str(node.content)
        if node.left != None:
            string += "L" + next(node.left)
        if node.right != None:
            string += "R" + next(node.right)
        return string
def add(node,n):
    if n < node.content:
        if node.left == None:
            Node = BNode()
            Node.content = n
            node.left = Node
        else:
            add(node.left,n)
    if n > node.content:
        if node.right == None:
            Node = BNode()
            Node.content = n
            node.right = Node
        else:
            add(node.right,n)
def find(node,n):
    if node.content == n:
        tree = BTree()
        tree.root = node
        return tree
    elif (node.left != None) and (node.content > n):
        return find(node.left,n)
    elif (node.right != None) and (node.content < n):
        return find(node.right,n)
    return None
class BTree():
    def __init__(self):
        self.root = None
    def __str__(self):
        if self.root == None:
            return "<<E>>"
        else:
            return next(self.root)
    def add(self,n):
        if self.root == None:
            root = BNode()
            root.content = n
            self.root = root
        else:
            add(self.root,n)
    def find(self,n):
        if self.root == None:
            return None
        else:
            return find(self.root,n)


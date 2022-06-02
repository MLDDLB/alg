class Node:

    def __init__(self, value):
        self.key = value
        self.parent = None
        self.left = None
        self.right = None

class BiTree:

    def __init__(self, value):
        self.root = Node(value)

    def Insert(self, value):
        nd = Node(value)
        x = self.root
        

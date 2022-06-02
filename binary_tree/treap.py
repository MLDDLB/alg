
class Node:

    def __init__(self, key = None, priority = None):
        self.key = key
        self.priority = priority
        self.left = None
        self.right = None
        self.parent = None

    def __str__(self):
        return f"({self.key}, {self.priority})"

class Treap:

    def __init__(self):
        self.root = None

    def split(self, key):
        x = self.root
        y = None
        while x is not None or x.key != key:
            y = x
            if key > x.key:
                x = x.right
            else:
                x = x.left
        if y is None:
            return None
        new_tree = Treap()
        new_tree.root = y
        if y == y.parent.left:
            y.parent.left = None
        else:
            y.parent.right = None
        return new_tree

    def merge(self, tree):
        if tree.root is None:
            return
        if tree.root.priority < self.root.priority:
            x = self.root
            y = None
            while x.priority > tree.root.priority:
                y = x
                x = x.right


    def insert(self, node):
        pass

    def delete(self, node):
        pass

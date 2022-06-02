from collections import deque
import sys

class TreapNode:

    def __init__(self, key, priority):
        self.key = key
        self.priority = priority
        self.parent = None
        self.left = None
        self.right = None

    def __str__(self):
        return str((self.key, self.priority))

class Treap:

    def __init__(self, treap_node = None):
        self.root = treap_node

    def __str__(self):
        dq = deque()
        res=''
        dq.append(self.root)
        i = 0
        j = 0
        while dq:
            x = dq.popleft()
            if x.left is not None:
                dq.append(x.left)
            if x.right is not None:
                dq.append(x.right)
            res += "{} ".format(x)
            i += 1
            if i >= 2**j:
                i = 0
                j += 1
                res +='\n'
        return res

    def inorder_tree_walk(self, node):
        if node is not None:
            self.inorder_tree_walk(node.left)
            print(node)
            self.inorder_tree_walk(node.right)

    @classmethod
    def split(cls, node, k):
        if node is None:
            return (None, None)
        elif k > node.key:
            (t1, t2) = cls.split(t.right, k)
            t.right = t1
            return (t, t2)
        else:
            (t1, t2) = cls.split(t.left, k)
            t.left = t2
            return (t1, t)

    @classmethod
    def merge(cls, t1, t2):
        if t2 is None:
            return t1
        if t1 is None:
            return t2
        elif t1.priority > t2.priority:
            t1.right = cls.merge(t1.right, t2)
            return t1
        else:
            t2.left = cls.merge(t1, t2.left)
            return t2

    def insert(self, node):
        x = self.root
        y = None
        while x is not None and x.priority > node.priority:
            y = x
            if node.key < x.key:
                x = x.left
            else:
                x = x.right
        if y is None and x is None:
            self.root = node
        else:
            (t1, t2) = Treap.split(x, node.key)
            node.left = t1
            node.right = t2
            node.parent = y
            if y is None:
                self.root = node
            else:
                if node.key > y.key:
                    y.right = node
                else:
                    y.left = node

    def delete(self, key):
        x = self.root
        y = None
        while x is not None and x.key != key:
            y = x
            if key > x.key:
                x = x.right
            else:
                x = x.left
        if x is None:
            return None
        else:
            new_t = Treap.merge(x.left, x.right)
            if new_t is not None:
                new_t.parent = y
            if y is None:
                self.root = new_t
            elif x is y.left:
                y.left = new_t
            else:
                y.right = new_t


t1 = Treap()
while inp := tuple(map(int, sys.stdin.readline().strip().split())):
    new_node = TreapNode(inp[0], inp[1])
    t1.insert(new_node)
print(t1)
t1.inorder_tree_walk(t1.root)
while inp := sys.stdin.readline().strip():
    key = int(inp)
    t1.delete(key)
t1.inorder_tree_walk(t1.root)

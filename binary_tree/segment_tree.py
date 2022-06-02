import sys
from collections import deque

class Interval:

    def __init__(self, low, high):
        self.low = low
        self.high = high

    def __str__(self):
        return "["+str(self.low)+","+str(self.high)+']'

    def intersects(self, y):
        if y.low <= self.high and self.low <= y.high:
            return True
        else:
            return False

class Node:

    def __init__(self, inter, parent = None, left = None, right = None ):
        self.parent = parent
        self.left = left
        self.right = right
        self.int = inter
        if inter is not None:
            self.max = inter.high
        else:
            self.max = float('-inf')
        self.color = 'black'

    def __str__(self):
        return f"[{self.int}, {self.color}, {self.max}]"

class SegmentTree:

    def __init__(self, root = None):
        self.root = root
        self.null = Node(None)
        if self.root == None:
            self.root = self.null
        self.null.left = self.null.right = self.root

    def __str__(self):
        dq = deque()
        res=''
        dq.append(self.root)
        i = 0
        j = 0
        while dq:
            x = dq.popleft()
            if x.left is not self.null:
                dq.append(x.left)
            if x.right is not self.null:
                dq.append(x.right)
            res += "{} ".format(x)
            i += 1
            if i >= 2**j:
                i = 0
                j += 1
                res +='\n'
        return res

    def inorder_tree_walk(self, x):
        if x is not self.null:
            self.inorder_tree_walk(x.left)
            print(x)
            self.inorder_tree_walk(x.right)

    def tree_minimum(self, node):
        x = node
        while x.left is not self.null:
            x = x.left
        return x

    def left_rotate(self, x):
        y = x.right
        x.right = y.left
        if y.left is not self.null:
            x.right.parent = x
        y.left = x
        if x.parent is self.null:
            self.root = y
        elif x == x.parent.left:
            x.parent.left = y
        else:
            x.parent.right = y
        y.parent = x.parent
        x.parent = y
        x.max = max(x.int.high, x.left.max, x.right.max)
        y.max = max(y.int.high, y.left.max, y.right.max)

    def right_rotate(self, x):
        y = x.parent
        y.left = x.right
        if y.left is not self.null:
            y.left.parent = x
        x.right = y
        if y.parent is self.null:
            self.root = x
        elif y == y.parent.left:
            y.parent.left = x
        else:
            y.parent.right = x
        x.parent = y.parent
        y.parent = x
        y.max = max(y.int.high, y.left.max, y.right.max)
        x.max = max(x.int.high, x.left.max, x.right.max)

    def insert(self, interval):
        new_node = Node(interval, left = self.null, right = self.null)
        x = self.root
        y = self.null
        while x is not self.null:
            if interval.high > x.max:
                x.max =interval.high
            y = x
            if new_node.int.low < x.int.low:
                x = x.left
            else:
                x = x.right
        new_node.parent = y
        if y is self.null:
            self.root = new_node
        elif new_node.int.low < y.int.low:
            y.left = new_node
        else:
            y.right = new_node
        new_node.color = 'red'
        self.insert_fixup(new_node)

    def insert_fixup(self, node):
        x = node
        while x.parent.color == 'red':
            if x.parent == x.parent.parent.left:
                y = x.parent.parent.right
                if y.color == 'red':
                    y.color = 'black'
                    x.parent.parent.color = 'red'
                    x.parent.color = 'black'
                    x = x.parent.parent
                else:
                    if x == x.parent.right:
                        x = x.parent
                        self.left_rotate(x)
                    x.parent.color = 'black'
                    x.parent.parent.color = 'red'
                    self.right_rotate(x.parent.parent)
            else:
                y = x.parent.parent.left
                if y.color == 'red':
                    y.color = 'black'
                    x.parent.parent.color = 'red'
                    x.parent.color = 'black'
                    x = x.parent.parent
                else:
                    if x == x.parent.left:
                        x = x.parent
                        self.right_rotate(x)
                    x.parent.color = 'black'
                    x.parent.parent.color = 'red'
                    self.left_rotate(x.parent.parent)
        self.root.color = 'black'

    def transplant(self, x, y):
        if x.parent is self.null:
            self.root = y
        elif x == x.parent.left:
            x.parent.left = y
        else:
            x.parent.right = y
        y.parent = x.parent

    def delete(self, node):
        y = node
        y_original_color = y.color
        if node.left is self.null:
            x = node.right
            self.transplant(node, node.right)
            #x.max = max(x.int.high, x.left.max, x.right.max)
        elif node.right is self.null:
            x = node.left
            self.transplant(node, node.left)
            #x.max = max(x.int.high, x.left.max, x.right.max)
        else:
            y = self.tree_minimum(node.right)
            y_original_color = y.color
            x = y.right
            if y.parent == node:
                x.parent = y
            else:
                self.transplant(y, y.right)
                y.right = node.right
                y.right.parent = y
                x.max = max(x.int.high, x.left.max, x.right.max)
            self.transplant(node, y)
            y.left = node.left
            y.left.parent = y
            y.color = node.color
            #y.max = max(y.int.high, y.left.max, y.right.max)
        if y_original_color == 'black':
            self.delete_fixup(x)

    def delete_fixup(self, node):
        x = node
        while x is not self.root and x.color == 'black':
            if x == x.parent.left:
                w = x.parent.right
                if w.color == 'red':
                    x.parent.color = 'red'
                    w.color = 'black'
                    self.left_rotate(x.parent)
                    w = x.parent.right
                if w.left.color == 'black' and w.right.color == 'black':
                    w.color = 'red'
                    x = x.parent
                else:
                    if w.right.color == 'black':
                        w.left.color = 'black'
                        w.color = 'red'
                        self.right_rotate(w)
                        w = x.parent.right
                    w.color = x.parent.color
                    x.parent.color = 'black'
                    w.right.color = 'black'
                    self.left_rotate(x.parent)
                    x = self.root
            else:
                w = x.parent.left
                if w.color == 'red':
                    x.parent.color = 'red'
                    w.color = 'black'
                    self.right_rotate(x.parent)
                    w = x.parent.left
                if w.right.color == 'black' and w.left.color == 'black':
                    w.color = 'red'
                    x = x.parent
                else:
                    if w.left.color == 'black':
                        w.right.color = 'black'
                        w.color = 'red'
                        self.left_rotate(w)
                        w = x.parent.left
                    w.color = x.parent.color
                    x.parent.color = 'black'
                    w.left.color = 'black'
                    self.right_rotate(x.parent)
                    x = self.root
        x.color = 'black'

    def search(self, inter):
        if type(inter) != Interval:
            raise TypeError("Wrong type")
        x = self.root
        while x is not self.null and not x.int.intersects(inter):
            if x.left is not self.null and x.left.max >= inter.low:
                x = x.left
            else:
                x = x.right
        return x

    def search_all(self, inter):
        x = self.root
        node_stack = [x,]
        node_list = []
        while node_stack:
            x = node_stack.pop()
            if x is not self.null and x.int.intersects(inter):
                node_list.append(x)
            if x.left is not self.null and x.left.max >= inter.low:
                node_stack.append(x.left)
            if x.right is not self.null and x.int.low <= inter.high and x.right.max >= inter.low:
                node_stack.append(x.right)
        return node_list


ST = SegmentTree()
while True:
    try:
        inp = sys.stdin.readline().strip().split()
        inter = Interval(int(inp[0]), int(inp[1]))
        print(inter)
        ST.insert(inter)
    except KeyboardInterrupt:
        print('done')
        break
print(ST)
print(ST.search(Interval(22, 25)))
ndl = ST.search_all(Interval(20, 20))
for i in ndl:
    print(i)
ST.delete(ST.root.left)
ST.inorder_tree_walk(ST.root)

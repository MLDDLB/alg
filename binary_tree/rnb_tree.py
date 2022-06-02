from collections import deque

class RnBNode:

    def __init__(self, key, parent = None, left = None, right = None):
        self.__key = key
        self.parent = parent
        self.left = left
        self.right = right
        self.__color = 'black'

    def __str__(self):
        return '({0}, {1})'.format(self.__key, self.__color)

    @property
    def key(self):
        return self.__key

    @key.setter
    def key(self, key):
        self.__key = key

    @property
    def color(self):
        return self.__color

    @color.setter
    def color(self, color):
        self.__color = color

class RnBTree:

    def __init__(self):
        self.NIL = RnBNode(None)
        self.root = self.NIL
        self.NIL.right = self.NIL.left = self.root

    def __str__(self):
        dq = deque()
        res=''
        dq.append(self.root)
        i = 0
        j = 0
        while dq:
            x = dq.popleft()
            if x.left is not self.NIL:
                dq.append(x.left)
            if x.right is not self.NIL:
                dq.append(x.right)
            res += "{} ".format(x)
            i += 1
            if i >= 2**j:
                i = 0
                j += 1
                res +='\n'
        return res

    def find(self, key):
        x = self.root
        while x is not self.NIL and x.key != key:
            if key < x.key:
                x = x.left
            else:
                x = x.right
        return x

    def tree_minimum(self, node):
        if type(node) != RnBNode:
            raise TypeError("Argument must be a node of the red-black tree.")
        x = node
        while x.left is not self.NIL:
            x = x.left
        return x

    def left_rotate(self, node):
        if type(node) != RnBNode:
            raise TypeError("Argument must be a node of the red-black tree.")
        y = node.right
        if y == self.NIL or node == self.NIL:
            raise ValueError("Can't rotate the NIL-node.")
        if y.left != self.NIL:
            y.left.parent = node
        if node is self.root:
            self.root = y
        elif node is node.parent.left:
            node.parent.left = y
        else:
            node.parnet.right = y
        y.parent = node.parent
        node.parent = y
        node.right = y.left
        y.left = node

    def right_rotate(self, node):
        if type(node) != RnBNode:
            raise TypeError("Argument must be a node of the red-black tree.")
        y = node.left
        if y is self.NIL or node is self.NIL:
            raise ValueError("Can't rotate the NIL-node.")
        if node is self.root:
            self.root = y
        elif node is node.parent.left:
            node.parent.left = y
        else:
            node.parent.right = y
        y.parent = node.parent
        node.parent = y
        node.left = y.right
        y.right = node

    def insert(self, key):
        new_node = RnBNode(key, left = self.NIL, right = self.NIL)
        y = self.NIL
        x = self.root
        while x is not self.NIL:
            y = x
            if key < x.key:
                x = x.left
            else:
                x = x.right
        new_node.parent = y
        if y is self.NIL:
            self.root = new_node
        elif key < y.key:
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
                    x.parent.color = 'black'
                    y.color = 'black'
                    x.parent.parent.color = 'red'
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
                    x.parent.color = 'black'
                    y.color = 'black'
                    x.parent.parent.color = 'red'
                    x = x.parent.parent
                else:
                    if x == x.parent.left:
                        x = x.parent
                        self.right_rotate(x)
                    x.parent.color = 'black'
                    x.parent.parent.color = 'red'
                    self.left_rotate(x.parent.parent)
        self.root.color = 'black'

    def transplant(self, node_1, node_2):
        if type(node_1) != RnBNode or type(node_2) != RnBNode:
            raise TypeError("Both arguments must be nodes")
        if node_1 is self.root:
            self.root = node_2
        elif node_1 is node_1.parent.left:
            node_1.parent.left = node_2
        else:
            node_1.parent.right = node_2
        node_2.parent = node_1.parent

    def delete(self, node):
        if type(node) != RnBNode:
            raise TypeError("Argument must be a node of the red-black tree")
        y = node
        y_original_color = y.color
        if node.left is self.NIL:
            x = node.right
            self.transplant(node, x)
        elif node.right is self.NIL:
            x = node.left
            self.transplant(node, x)
        else:
            y = self.tree_minimum(node)
            y_original_color = y.color
            x = y.right
            if y.parent is node:
                x.parent = y
            else:
                self.transplant(y, y.right)
                y.right = node.right
                y.right.parent = y
            self.transplant(node, y)
            y.left = node.left
            y.left.parent = y
            y.color = node.color
        if y_original_color == 'black':
            self.delete_fixup(x)

    def delete_fixup(self, node):
        x = node
        while x is not self.root and x.color == 'black':
            if x == x.parent.left:
                w = x.parent.right
                if w.color == 'red':
                    w.color = 'black'
                    x.parent.color = 'red'
                    self.left_rotate(x.parent)
                    w = x.parent.right
                if w.left.color == w.right.color == 'black':
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
            if x == x.parent.right:
                w = x.parent.left
                if w.color == 'red':
                    w.color = 'black'
                    x.parent.color = 'red'
                    self.right_rotate(x.parent)
                    w = x.parent.left
                if w.left.color == w.right.color == 'black':
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


rnb_node = RnBNode(3)
print("node = {}".format(rnb_node))
rnb_tree = RnBTree()
while True:
    try:
        key = int(input('Enter key: '))
        rnb_tree.insert(key)
    except KeyboardInterrupt:
        print("done")
        break
print(rnb_tree)
while True:
    try:
        key = int(input('Enter key: '))
        elem = rnb_tree.find(key)
        rnb_tree.delete(elem)
        print('\n' + str(rnb_tree))
    except KeyboardInterrupt:
        print("done")
        break

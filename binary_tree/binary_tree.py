from collections import deque

class Node:

    def __init__(self, key, data = None):
        self.__key = key
        self.__data = data
        self.parent = None
        self.left = None
        self.right = None

    def __str__(self):
        return '({}: {})'.format(self.__key, self.__data)

    @property
    def key(self):
        return self.__key

    @property
    def data(self):
        return self.__data

class BinaryTree:

    def __init__(self):
        self.head = None

    def __str__(self):
        dq = deque()
        res=''
        dq.append(self.head)
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

    def insert(self, key):
        new_node = Node(key)
        y = None
        x = self.head
        while x is not None:
            y = x
            if new_node.key < x.key:
                x = x.left
            else:
                x = x.right
        new_node.parent = y
        if y is None:
            self.head = new_node
            return
        if new_node.key < y.key:
            y.left = new_node
            return
        else:
            y.right = new_node
            return

    def search(self, key):
        x = self.head
        while x is not None:
            if x.key == key:
                return x
            elif key < x.key:
                x = x.left
            else:
                x = x.right
        return x

    def delete(self, node):
        if type(node) != Node:
            raise TypeError("Argumnet must be a tree 'Node'")
        if node.left is None:
            node = node.right
        elif node.right is None:
            node = node.left
        else:
            succ = self.tree_minimum(node.right)
            if succ != node.right:
                self.transplant(succ, succ.right)
                succ.right = node.right
                succ.right.parent = succ
            self.transplant(node, succ)
            succ.left = node.left
            succ.left.parent = succ


    def transplant(self, first_node, second_node):
        if first_node.parent is None:
            self.head = second_node
        elif first_node == first_node.parent.left:
            first_node.parent.left = second_node
        else:
            first_node.parent.right = second_node
        if second_node is not None:
            second_node.parent = first_node.parent

    def tree_minimum(self, node):
        if type(node) != Node:
            raise TypeError("Argument must be a tree 'Node'")
        x = node
        while x.left != None:
            x = x.left
        return x

    def tree_maximum(self, node):
        if type(node) != Node:
            raise TypeError("Argument must be a tree 'Node'")
        x = node
        while x.right != None:
            x = x.right
        return x

    def get_successor(self, node):
        if type(node) != Node:
            raise TypeError("Argument must be a tree 'Node'")
        x = node
        if x.right is not None:
            return self.tree_minimum(x.right)
        y = x.p
        while y is not None and x != y.right:
            x = y
            y = y.p
        return y

    def get_predecessor(self, node):
        if type(node) != Node:
            raise TypeError("Argumnet must be a tree 'Node'")
        x = node
        if x.left is not None:
            return self.tree_maximum(x.left)
        y = x.p
        while y is not None and x != y.left:
            x = y
            y = y.p
        return y

    def inorder_tree_walk(self, node):
        if node is not None:
            self.inorder_tree_walk(node.left)
            print(node)
            self.inorder_tree_walk(node.right)

def __main__():
    bt = BinaryTree()
    while True:
        try:
            key = int(input('Enter key: '))
            bt.insert(key)
        except KeyboardInterrupt:
            print("done")
            break
    bt.inorder_tree_walk(bt.head)
    print(bt.tree_minimum(bt.head))
    print(bt)
    x = bt.search(15)
    print("x = {}".format(x))
    print("succ = {}".format(bt.get_successor(x)))
    bt.delete(x)
    print(bt)
    y = bt.search(18)
    print("y = {}, y.left = {}, y.right = {}".format(y, y.left, y.right))
    print("y.left.left = {}, y.left.right = {}".format(y.left.left, y.left.right))

if __name__ == '__main__':
    __main__()

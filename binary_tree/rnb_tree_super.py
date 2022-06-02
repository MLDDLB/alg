#super() = Function used to give access to the methods of a parent class.
#          Returns a temporary object of a parent class when used

import binary_tree

class RnBNode(binary_tree.Node):

    def __init__(self, key, data = None,color = 'black'):
        super().__init__(key, data)
        self.__color = 'black'

    def __str__(self):
        res = super().__str__()
        res += str(self.color)
        return res

    @property
    def color(self):
        return self.__color

class RnBTree(binary_tree.BinaryTree):

    def __init__(self):
        self.NIL = RnBNode(None)
        self.head = self.NIL
        self.NIL.right = self.NIL.left = self.head

a = RnBNode(13, 'f')
print("a = {}".format(a))
print("a.key = {0}, a.data = {1}, a.color = {2}".format(a.key, a.data, a.color))
rnb_tree = RnBTree()
rnb_tree.insert(2)
rnb_tree.insert(3)
rnb_tree.insert(1)
print(rnb_tree)

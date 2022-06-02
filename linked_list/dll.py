class Node:

    def __init__(self, value, next = None, prev = None):
        self.key = value
        self.next = next
        self.previous = prev

    def __str__(self):
        return str(self.key)


class DLList:

    def __init__(self):
        self.Head = Node(None)
        self.Head.next = self.Head
        self.Head.previous = self.Head

    def Insert(self, value, elem = None):
        nd = Node(value)
        if elem is None:
            elem = self.Head
        if type(elem) != Node:
            raise TypeError("Element must be a node")
        nd.next = elem.next
        elem.next.previous = nd
        elem.next = nd
        nd.previous = elem

    def Delete(self, elem = None):
        if elem is None:
            elem = self.Head.previous
        if elem is self.Head:
            raise IndexError("No such element in the list or list is empty")
        elif type(elem) != Node:
            raise TypeError("Element must be a node")
        elem.next.previous = elem.previous
        elem.previous.next = elem.next

    def Search(self, key):
        x = self.Head.next
        while x.key != None and x.key != key:
            x = x.next
        return x

    def Unify(self, list_2):
        if type(list_2) != DLList:
            raise TypeError("Argument must be a linked list")
        self.Head.previous.next = list_2.Head.next
        list_2.Head.previous.next = self.Head

    def __str__(self):
        res = str()
        x = self.Head.next
        while x.key != None:
            res += "{} <-> ".format(x.key)
            x = x.next
        return res

a = DLList()
while True:
    try:
        a.Insert(int(input()))
    except KeyboardInterrupt:
        break
print("a = {}".format(a))
print("a[1] = {}".format(a.Head.next.key))
y = a.Search(6)
print("y = {}".format(y.key))
a.Delete(y)
print("a = {}".format(a))
a.Insert(3, a.Head.previous)
print("a = {}".format(a))
b = DLList()
while True:
    try:
        b.Insert(int(input()))
    except KeyboardInterrupt:
        break
print("b = {}".format(b))
a.Unify(b)
print("a = {}".format(a))

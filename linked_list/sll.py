class sll_obj:

    def __init__(self, val):
        self.key = val
        self.next = None

class SLList:

    def __init__(self):
        self.Head = sll_obj(None)
        self.Head.next = self.Head

    def Search(self, key):
        x = self.Head.next
        while x.key != None and x.key != key:
            x = x.next
        return x

    def Insert(self, val, elem = None):
        so = sll_obj(val)
        if elem == None:
            so.next = self.Head.next
            self.Head.next = so
        else:
            so.next = elem.next
            elem.next = so

    def Delete(self, elem = None):
        if elem == None:
            if self.Head.next == self.Head:
                raise IndexError("List is empty")
            else:
                self.Head.next = self.Head.next.next
        else:
            if elem.next.key == None:
                raise IndexError("Can't delete the NULL element")
            elem.next = elem.next.next

    def Unify(self, list_2):
        if type(list_2) != SLList:
            raise TypeError("Argument should be a linked list")
        x = self.Head.next
        while x.next.key != None:
            x = x.next
        x.next = list_2.Head.next


    def __str__(self):
        res = str()
        x = self.Head.next
        while x.key != None:
            res += "{} -> ".format(x.key)
            x = x.next
        return res

a = SLList()
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
a.Insert(3, y)
print("a = {}".format(a))
b = SLList()
while True:
    try:
        b.Insert(int(input()))
    except KeyboardInterrupt:
        break
print("b = {}".format(b))
a.Unify(b)
print("a = {}".format(a))

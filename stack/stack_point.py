class Stack_object:

    def __init__(self, value):
        self.next = None
        self.prev = None
        self.val = value


class Stack:

    def __init__(self):
        self.Head = Stack_object(None)

    def Push(self, value):
        x = Stack_object(value)
        if self.Head.val is None:
            self.Head = x
            x.next = None
            x.prev = None
        else:
            x.next = self.Head
            self.Head.prev = x
            x.prev = None
            self.Head = x

    def __str__(self):
        x = self.Head
        res = str()
        while x is not None:
            res += " {}".format(x.val)
            x = x.next
        return res

mys = Stack()
mys.Push(1)
mys.Push(2)
mys.Push(3)
print("stack = {}".format(mys))

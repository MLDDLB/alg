class Stack_object:
    def __init__(self, value):
        self.key = value
        self.next = None


class Stack:

    def __init__(self):
        self.Tail = Stack_object(None)

    def Push(self, x):
        so = Stack_object(x)
        so.next = self.Tail
        self.Tail = so

    def Pop(self):
        if self.Tail.key == None:
            raise IndexError("stack is empty")
        res = self.Tail.key
        self.Tail = self.Tail.next
        return res

    def __str__(self):
        res = str()
        x = self.Tail
        while x.key != None:
            res += "{} -> ".format(x.key)
            x = x.next
        return res

mys = Stack()
while True:
    x = int(input())
    if x == -1:
        break
    mys.Push(x)
print("finished")
print(mys)
while True:
    try:
        print("pop = {}".format(mys.Pop()))
        print(mys)
    except IndexError:
        print("is empty")
        break

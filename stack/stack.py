class Stack:

    def __init__(self, value = list()):
        try:
            n = len(value)
            self.Top = n
            self.List = value
            print("self.top = {}; self.List = {}".format(self.Top, self.List))
        except:
            self.Too = 1
            self.List = list(value)

    def IsEmpty(self):
        if self.Top == 0:
            return True
        else:
            return False

    def Push(self, val):
        self.Top += 1
        self.List.append(val)

    def Pop(self):
        if self.IsEmpty():
            raise IndexError("Underflow")
        else:
            res = self.List[self.Top - 1]
            del(self.List[self.Top - 1])
            self.Top -= 1
            return res

    def __str__(self):
        return str(self.List)


a = Stack()
print("a = {}".format(a))
a.Push(1)
a.Push(2)
print("a = {}".format(a))
print("a.top = {}".format(a.Pop()))
print("a = {}".format(a))

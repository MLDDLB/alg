class Stack:

    def __init__(self, value = []):
        try:
            n = len(value)
            self.Top = n
            self.List = value
        except:
            n = 1
            self.Top = n
            self. List = list(value)

    def IsEmpty(self):
        if self.Top == 0:
            return True
        else: return False

    def Push(self, value):
        self.Top += 1
        self.List.append(value)

    def Pop(self):
        return self.List.pop()

    def __str__(self):
        return str(self.List)

a = Stack()
print("a = {}; a = {}".format(a, a.List))
a.Push(1)
a.Push(2)
print("a = {}".format(a))
print("a.top = {}".format(a.Pop()))
print("a = {}".format(a))
a.Pop()
a.Pop()

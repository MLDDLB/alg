from collections import deque

class Stack:

    def __init__(self, value = []):
        try:
            n = len(value)
            self.Top = n
            self.List = deque(value)
        except TypeError:
            n = 1
            self.Top = 1
            self.List = deque(value)

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

a = Stack([1, 2])
print("a = {}".format(a))
a.Push(1)
a.Push(2)
print("a = {}".format(a))
print("a.top = {}".format(a.Pop()))
print("a = {}".format(a))

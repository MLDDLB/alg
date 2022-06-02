from collections import deque

class Queue:

    def __init__(self, value = [], ml = None):
        try:
            n = len(value)
            self.List = deque(value, maxlen = ml)
            self.Length = len(self.List)
        except:
            self.List = deque(maxlen = ml)
            self.List.append(value)
            self.Length = len(self.List)

    def Enque(self, value):
        self.List.append(value)

    def Deque(self):
        return self.List.popleft()

    def __str__(self):
        return str(self.List)

a = Queue(2, 5)
print("a = {}".format(a))
a.Enque(3)
a.Enque(4)
print("a = {}".format(a))
print("a[0] = {}".format(a.Deque()))
print("a = {}".format(a))
a.Enque(3)
a.Enque(4)
a.Enque(5)
a.Enque(6)
print("a = {}".format(a))
a.Enque(7)
print("a = {}".format(a))

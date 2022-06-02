class Queue:

    def __init__(self, value = [], maxlen = None):
        if maxlen is not None and type(maxlen) == int:
            self.Length = maxlen
            if self.Length <= 0:
                raise ValueError("length must be an integer number greater than 0")
        try:
            n = len(value)
            if maxlen is None:
                self.Length = n
            elif n > maxlen:
                raise ValueError("length of the iterable is greater than maxlen")
            self.List = value
        except:
            if maxlen is None:
                self.Length = 1
            self.List = [value]


    def Enque(self, value):
        if len(self.List) + 1 > self.Length:
            raise IndexError("Queue is full")
        self.List.append(value)

    def Deque(self):
        return self.List.pop(0)

    def __str__(self):
        return str(self.List)

a = Queue(2, 5)
print("a = {}".format(a))
a.Enque(3)
a.Enque(4)
print("a = {}".format(a))
print("a[0] = {}".format(a.Deque()))

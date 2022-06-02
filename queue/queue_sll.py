class Queue_object:

    def __init__(self, value):
        self.key = value
        self.next = None

class Queue:

    def __init__(self):
        self.Head = Queue_object(None)
        self.Tail = self.Head

    def Enqueue(self, value):
        qo = Queue_object(value)
        if self.Tail is self.Head:
            self.Tail = qo
            self.Head.next = qo
            qo.next = self.Head
        else:
            self.Tail.next = qo
            self.Tail = qo
            qo.next = self.Head

    def Dequeue(self):
        if self.Head.next is self.Head or self.Head is self.Tail:
            raise IndexError("Queue is empty")
        x = self.Head.next
        self.Head.next = x.next
        return x.key

    def __str__(self):
        res = str()
        x = self.Head.next
        while x.key is not None:
            res += "{} <- ".format(x.key)
            x = x.next
        res += "end"
        return res

myq = Queue()
while True:
    try:
        myq.Enqueue(int(input()))
    except KeyboardInterrupt:
        break
print(myq)
while True:
    try:
        print("Dequeue = {}".format(myq.Dequeue()))
        print(myq)
    except IndexError:
        print("is empty")
        break

class Graph:


    def __init__(self):
        self.V = {}

    def insert(self, *args):
        print(args)
        for i in args:
            self.V[i.key] = i

    def __getitem__(self, key):
        return self.V[key]

    def __iter__(self):
        return iter(self.V)


class Vertex:

    def __init__(self, val=None, parent=None, color=0, distance=0):
        self.key = val
        self.edges = []
        self.parent = parent
        self.color = color
        self.distance = distance

    def __iter__(self):
        return iter(self.edges)

    def __repr__(self):
        return repr(self.key)

    def __str__(self):
        return str(self.key)

    def add_edge(self, *args):
        for i in args:
            self.edges.append(i)

import collections.abc

class MinHeap:

    def __init__(self, val):
        if isinstance(val, collections.abc.Iterable):
            self.heap_size = len(val)
            self.list = val
        else:
            self.heap_size = 1
            self.list = [val]
        n = (len(self.list)-1)//2
        print(f"list = {self.list}, heap_size = {self.heap_size}, n = {n}")
        for i in range(n, -1, -1):
            self.min_heapify(i)

    def __getitem__(self, key):
        return self.list[key]

    def __setitem__(self, key, value):
        self.list[key] = value

    def get_left(self, i):
        if 2*i+1 < self.heap_size:
            return 2*i+1
        else:
            return None

    def get_right(self, i):
        if 2*i+2 < self.heap_size:
            return 2*i+2
        else:
            return None

    def get_parent(self, i):
        if i >= 1:
            if i%2 == 0:
                return (i//2 - 1)
            else:
                return i//2
        else:
            return i

    def get_min(self):
        if heap_size >= 1:
            return self[0]
        else:
            return None

    def extract_min(self):
        minimum = self[0]
        self.delete(0)
        return minimum

    def min_heapify(self, i):
        left = self.get_left(i)
        right = self.get_right(i)
        if left is not None and self[left] < self[i]:
            smallest = left
        else:
            smallest = i
        if right is not None and self[right] < self[smallest]:
            smallest = right
        if smallest != i:
            buf = self[i]
            self[i] = self[smallest]
            self[smallest] = buf
            self.min_heapify(smallest)

    def decrease_key(self, i, key):
        if key >= self[i]:
            raise ValueError
        self[i] = key
        while i >= 0 and self[i] >= self[self.get_parent(i)]:
            buf = self[i]
            self[i] = self[self.get_parent(i)]
            self[self.get_parent(i)] = buf
            i = self.get_parent(i)

    def insert(self, key):
        self.heap_size += 1
        self.list.append(float('inf'))
        self.decrease_key(len(self.list) - 1, key)

    def delete(self, key):
        self[key] = self[self.heap_size-1]
        self.heap_size -= 1
        del(self[heap_size])
        self.min_heapify(key)


def huffman(c):
    n = len(c)
    Q = MinHeap(c)
    for i in range(1, n):
        z = TreeNode()
        x = Q.ExtractMin()
        y = Q.ExratctMin()
        z.key = x.key + y.key
        z.left = x
        z.right = y
        Q.insert(z)
    return Q.get_min

arr = [15, 6, 14, 2, 26, 13, 5, 3, 1, 20]
my_heap = MinHeap(arr)
print(my_heap.list)

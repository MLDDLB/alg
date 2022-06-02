class heap:

    def __init__(self, value):
        try:
            self.HeapSize = len(value)
            self.List = value
        except ValueError:
            self.HeapSize = 1
            self.List = list(value)

    def __getitem__(self, key):
        return self.List[key]

    def __len__(self):
        return self.HeapSize

    def __str__(self):
        return str(self.List)

    def GetParent(self, i):
        if i > 1:
            return i//2
        else:
            return i
    def GetLeft(self, i):
        return 2*i + 1

    def GetRight(self, i):
        return 2*i + 2




class Max_heap(heap):

    def Max_Heapify(self, i):
        while i < len(self):
            print("i = {}".format(i))
            left = self.GetLeft(i)
            print("left = {}".format(left))
            right = self.GetRight(i)
            print("right = {}".format(right))
            largest = left if left < len(self) and self.List[left] > self.List[i] else i
            if right < len(self) and self.List[right] > self.List[largest]:
                largest = right
            if largest != i:
                print("largest = {}".format(largest))
                buf = self.List[i]
                self.List[i] = self.List[largest]
                self.List[largest] = buf
                i = largest
                continue
            break

    def __init__(self, value):
            try:
                self.HeapSize = len(value)
                self.List = value
            except ValueError:
                self.HeapSize = 1
                self.List = list(value)
            n = (len(value) - 1)//2
            for i in range(n, -1, -1):
                self.Max_Heapify(i)


class Min_heap(heap):

    def Min_Heapify(self, i):
        print("i = {}".format(i))
        left = self.GetLeft(i)
        print("left = {}".format(left))
        right = self.GetRight(i)
        print("right = {}".format(right))
        smallest = left if left < len(self) and self.List[left] < self.List[i] else i
        if right < len(self) and self.List[right] < self.List[smallest]:
            smallest = right
        if smallest != i:
            print("largest = {}".format(smallest))
            buf = self.List[i]
            self.List[i] = self.List[smallest]
            self.List[smallest] = buf
            self.Min_Heapify(smallest)

    def __init__(self, value):
            try:
                self.HeapSize = len(value)
                self.List = value
            except ValueError:
                self.HeapSize = 1
                self.List = list(value)
            n = (len(value) - 1)//2
            for i in range(n, -1, -1):
                self.Min_Heapify(i)

def HeapSort(arr):
    heap = Max_heap(arr)
    n = len(arr)
    for i in range(n, 0, -1):
        buf = heap.List[0]
        heap.List[0] = heap.List[i]
        heap.List[i] = buf
        heap.HeapSize -= 1
        heap.Max_Heapify(0)

numList = []
while True:
    try:
        num = int(input("Enter a number: "))
    except:
        print("Enter an integer number")
        continue
    if num == -1:
        break
    numList.append(num)
print(numList)
myHeap1 = Max_heap(numList)
print(myHeap1)
myHeap2 = Min_heap(numList)
print(myHeap2)

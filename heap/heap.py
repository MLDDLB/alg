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
        if i >= 1:
            if i%2 == 0:
                return (i//2 - 1)
            else:
                return i//2
        else:
            return i
    def GetLeft(self, i):
        return 2*i + 1

    def GetRight(self, i):
        return 2*i + 2




class Max_heap(heap):

    def Max_Heapify(self, i):
        #print("i = {}".format(i))
        left = self.GetLeft(i)
        #print("left = {}".format(left))
        right = self.GetRight(i)
        #print("right = {}".format(right))
        largest = left if left < len(self) and self.List[left] > self.List[i] else i
        if right < len(self) and self.List[right] > self.List[largest]:
            largest = right
        if largest != i:
            #print("largest = {}".format(largest))
            buf = self.List[i]
            self.List[i] = self.List[largest]
            self.List[largest] = buf
            self.Max_Heapify(largest)

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

    def GetMax(self):
        return self[0]

    def ExtractMax(self):
        if len(self) == 0:
            raise ValueError("The que is empty")
        max = self.List[0]
        self.List[0] = self.List[len(self) - 1]
        del(self.List[len(self) - 1])
        self.HeapSize -= 1
        self.Max_Heapify(0)
        return max

    def IncreaseKey(self, i, key):
        if key < self[i]:
            raise ValueError("The new key is less than the current one")
        self.List[i] = key
        while i >= 0 and self[self.GetParent(i)] < self.List[i]:
            buf = self.List[self.GetParent(i)]
            self.List[self.GetParent(i)] = self.List[i]
            self.List[i] = buf
            i = self.GetParent(i)

    def Insert(self, key):
        self.HeapSize += 1
        self.List.append(float('-inf'))
        self.IncreaseKey(self.HeapSize - 1, key)

    def Delete(self, key):
        self.List[key] = self.List[self.HeapSize - 1]
        del(self.List[self.HeapSize - 1])
        self.HeapSize -= 1
        self.Max_Heapify(key)


class Min_heap(heap):

    def Min_Heapify(self, i):
        #print("i = {}".format(i))
        left = self.GetLeft(i)
        #print("left = {}".format(left))
        right = self.GetRight(i)
        #print("right = {}".format(right))
        smallest = left if left < len(self) and self.List[left] < self.List[i] else i
        if right < len(self) and self.List[right] < self.List[smallest]:
            smallest = right
        if smallest != i:
            #print("largest = {}".format(smallest))
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

    def GetMin(self):
        return self[0]

    def ExtractMin(self):
        if len(self) == 0:
            raise ValueError("The que is empty")
        min = self.List[0]
        self.List[0] = self.List[len(self) - 1]
        del(self.List[len(self) - 1])
        self.HeapSize -= 1
        self.Min_Heapify(0)
        return min

    def DecreaseKey(self, i, key):
        if key > self[i]:
            raise ValueError("The new key is less than the current one")
        self.List[i] = key
        while i >= 0 and self[self.GetParent(i)] > self.List[i]:
            buf = self.List[self.GetParent(i)]
            self.List[self.GetParent(i)] = self.List[i]
            self.List[i] = buf
            i = self.GetParent(i)

    def Insert(self, key):
        self.HeapSize += 1
        self.List.append(float('inf'))
        self.DecreaseKey(self.HeapSize - 1, key)

    @classmethod
    def HeapSort(cls, arr):
        heap = Min_heap(arr)
        for i in range(heap.HeapSize - 1, 0, -1):
            buf = heap.List[0]
            heap.List[0] = heap.List[i]
            heap.List[i] = buf
            heap.HeapSize -= 1
            heap.Min_Heapify(0)


'''def HeapSort(arr):
    heap = Max_heap(arr)
    n = len(arr)
    for i in range(n - 1, 0, -1):
        buf = heap.List[0]
        heap.List[0] = heap.List[i]
        heap.List[i] = buf
        heap.HeapSize -= 1
        heap.Max_Heapify(0)'''



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
numList2 = numList.copy()
myHeap2 = Min_heap(numList2)
print(myHeap2)
srtdList = numList.copy()
Min_heap.HeapSort(srtdList)
print("list = {}".format(srtdList))
print("max = {}".format(myHeap1.GetMax()))
max1 = myHeap1.ExtractMax()
print("max1 = {}, heap = {}".format(max1, myHeap1))
myHeap1.IncreaseKey(5, 15)
print("heap = {}".format(myHeap1))
myHeap1.Insert(16)
print("heap = {}".format(myHeap1))
myHeap1.Delete(5)
print("heap = {}".format(myHeap1))
print("heap_min = {}".format(myHeap2))
print("min = {}".format(myHeap2.GetMin()))
min1 = myHeap2.ExtractMin()
print("min1 = {}, heap_min = {}".format(min1, myHeap2))
myHeap2.DecreaseKey(5, -1)
print("heap = {}".format(myHeap2))
myHeap2.Insert(16)
print("heap = {}".format(myHeap2))

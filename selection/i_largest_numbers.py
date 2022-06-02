import time
import selection

def Merge(arr, p, q, r):
    L = [i for i in arr[p:q+1]]
    print("L = {}".format(L))
    R = [j for j in arr[q+1:r+1]]
    print("R = {}".format(R))
    n1 = len(L)
    n2 = len(R)
    i = 0
    j = 0
    for k in range(p, r+1):
        try:
            if L[i] <= R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
        except:
            #if k == r:
                #break
            if i >= n1:
                arr[k] = R[j]
                j += 1
            elif j >= n2:
                arr[k] = L[i]
                i += 1
    return()

def MergeSort(arr, p, r):
    if p < r:
        q = (r+p)//2
        print(" p = {} r = {} q = {}".format(p,r,q))
        MergeSort(arr, p, q)
        print("finished 1")
        MergeSort(arr, q+1, r)
        print("finished 2")
        Merge(arr, p, q, r)
        print("list: {}".format(arr))
    return()

def GetLargest1(arr, i):
    if i > len(arr):
        raise ValueError("i is larger than the size of the list")
    MergeSort(arr, 0, len(arr) - 1)
    ordList = list()
    n = len(arr)
    for j in range(n - 1, n - 1 - i, -1):
        ordList.append(arr[j])
    return ordList

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
        print("len = {}".format(len(self)))
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

    def HeapSort(self):
        for i in range(self.HeapSize, 0, -1):
            buf = heap.List[0]
            heap.List[0] = heap.List[i]
            heap.List[i] = buf
            heap.HeapSize -= 1
            heap.Min_Heapify(0)

def HeapSort(arr):
    heap = Max_heap(arr)
    n = len(arr)
    for i in range(n - 1, 0, -1):
        buf = heap.List[0]
        heap.List[0] = heap.List[i]
        heap.List[i] = buf
        heap.HeapSize -= 1
        heap.Max_Heapify(0)

def GetLargest2(arr, i):
    if i > len(arr):
        raise ValueError
    hp = Max_heap(arr)
    print("heap = {}".format(hp))
    ordList = list()
    for j in range(0, i):
        ordList.append(hp.ExtractMax())
    return ordList

def GetLargest3(arr, i):
    n = len(arr)
    x = selection.Select(arr, 0, n - 1, n - i)
    ind = selection.Partition(arr, 0, n - 1, x)
    selection.InsertSort(arr, ind, n - 1)
    ordList = list()
    for j in range(n - 1, ind - 1, -1):
        ordList.append(arr[j])
    return ordList

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
numList_2 = numList.copy()
numList_3 = numList.copy()
clock = time.time()
ordList = GetLargest1(numList, int(input("Number of statistics you want to get: ")))
print("ordList = {}; time = {}".format(ordList, time.time() - clock))
clock = time.time()
ordList = GetLargest2(numList_2, int(input("Number of statistics you want to get: ")))
print("ordList = {}; time = {}".format(ordList, time.time() - clock))
clock = time.time()
ordList = GetLargest3(numList_3, int(input("Number of statistics you want to get: ")))
print("ordList = {}; time = {}".format(ordList, time.time() - clock))

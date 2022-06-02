import random

def Partition(arr, beg, end):
    x = arr[end]
    i = beg - 1
    for j in range(beg, end):
        if arr[j] <= x:
            i = i + 1
            buf = arr[j]
            arr[j] = arr[i]
            arr[i] = buf
    buf = arr[end]
    arr[end] = arr[i + 1]
    arr[i + 1] = buf
    return i + 1

def RandomizedPartition(arr, beg, end):
    rnd = random.randint(beg, end)
    buf = arr[end]
    arr[end] = arr[rnd]
    arr[rnd] = buf
    return Partition(arr, beg, end)

def RandomizedQuickSort(arr, beg, end):
    if beg < end:
        q = RandomizedPartition(arr, beg, end)
        RandomizedQuickSort(arr, beg, q - 1)
        RandomizedQuickSort(arr, q + 1, end)

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
print("list = {}".format(numList))
RandomizedQuickSort(numList, 0, len(numList) - 1)
print("sorted list = {}".format(numList))

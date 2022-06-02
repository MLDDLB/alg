import random

def Partition(arr, beg, end):
    x = arr[end]
    i = beg - 1
    for j in range(beg, end):
        if arr[j] <= x:
            i += 1
            buf = arr[j]
            arr[j] = arr[i]
            arr[i] = buf
    buf = arr[i + 1]
    arr[i + 1] = x
    arr[end] = buf
    return (i + 1)

def RandomizedPartition(arr, beg, end):
    rnd = random.randint(beg, end)
    buf = arr[end]
    arr[end] = arr[rnd]
    arr[rnd] = buf
    return Partition(arr, beg, end)

def RandSelect(arr, beg, end, i):
    if beg == end:
        return arr[beg]
    q = RandomizedPartition(arr, beg, end)
    k = q - beg + 1
    if k == i:
        return arr[q]
    elif k < i:
        return RandSelect(arr, q + 1, end, i - k)
    else:
        return RandSelect(arr, beg, q - 1, i)

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
i = int(input("Enter the number of order statistic: "))
print("The {} order statistic = {}".format(i, RandSelect(numList, 0, len(numList) - 1, i)))

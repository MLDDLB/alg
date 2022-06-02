def Partition(arr, beg, end):
    x = arr[end]
    i = beg - 1
    for j in range(beg, end):
        if arr[j] <= x:
            i = i + 1
            buf = arr[j]
            arr[j] = arr[i]
            arr[i] = buf
    buf = arr[end - 1]
    arr[end - 1] = arr[i + 1]
    arr[i + 1] = buf
    return i + 1

def QuickSort(arr, beg, end):
    if beg < end:
        q = Partition(arr, beg, end)
        QuickSort(arr, beg, q - 1)
        QuickSort(arr, q + 1, end)

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
QuickSort(numList, 0, len(numList) - 1)
print("sorted list = {}".format(numList))

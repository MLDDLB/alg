def Partition(arr, beg, end):
    x = arr[end - 1]
    i = beg - 1
    for j in range(beg, end - 1):
        if arr[j] <= x:
            i += 1
            buf = arr[j]
            arr[j] = arr[i]
            arr[i] = buf
    buf = arr[i + 1]
    arr[i + 1] = arr[end - 1]
    arr[end - 1] = buf
    return (i+1)

def QuickSort(arr, beg, end):
    if beg < end:
        q = Partition(arr, beg, end)
        QuickSort(arr, beg, q)
        QuickSort(arr, q + 1, end)

def FindWeightedMed(arr):
    n = len(arr)
    if n == 1:
        return arr[0]
    i = 0
    sum = 0
    while sum < 1/2:
        sum += arr[i]
        i += 1
    return (i - 1)

numList = []
while True:
    try:
        num = float(input("Enter a number: "))
    except:
        print("Enter an integer number")
        continue
    if num == -1:
        break
    numList.append(num)
print("list = {}".format(numList))
QuickSort(numList, 0, len(numList))
print("sorted list = {}".format(numList))
wMed = FindWeightedMed(numList)
print("Weighted median = {}".format(wMed))

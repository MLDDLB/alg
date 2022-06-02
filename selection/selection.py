def InsertSort(arr, beg = 0, end = -1):
    if end == -1:
        end = len(arr)
    print("beg = {}; end = {}".format(beg, end))
    for i in range(beg, end):
        print("arr[{}] = {}".format(i, arr[i]))
        key = arr[i]
        j = i - 1
        while j >= beg and arr[j] >= key:
            arr[j+1] = arr[j]
            j -= 1
        arr[j + 1] = key

def Partition(arr, beg, end, x):
    i = beg - 1
    print("partS = {}, pBeg = {}, pEnd = {}".format(arr, beg, end))
    ind = -1
    for j in range(beg, end + 1):
        if arr[j] <= x:
            i += 1
            buf = arr[j]
            arr[j] = arr[i]
            arr[i] = buf
            if arr[i] == x:
                ind = i
                print("ind = {}".format(ind))
    print("partE = {}; pivot = {}".format(arr, x))
    if ind > 0:
        buf = arr[i]
        arr[i] = arr[ind]
        arr[ind] = buf
    return i

def Select(arr, beg, end, i):
    if beg == end:
        return arr[beg]
    n = end - beg + 1
    if n%5 == 0:
        m = n//5
    else:
        m = n//5 + 1
    medList = list()
    for j in range(1, m + 1):
        if j * 5 <= n:
            #print("beg = {}; end = {}".format(beg + (j - 1)*5, j*5))
            InsertSort(arr, beg + (j - 1)*5, beg + j*5)
            medList.append(arr[(2*beg + j*10 - 5)//2])
        else:
            #print("beg = {}; end = {}".format(beg + (j - 1)*5, n))
            InsertSort(arr, beg + (j - 1)*5, beg + n)
            medList.append(arr[(2*beg + (j - 1)*5 + n)//2])
        print("arr = {}".format(arr))
        print("med = {}".format(medList))
    mainMed = Select(medList, 0, len(medList) - 1, len(medList)//2)
    print("mainMed = {}".format(mainMed))
    q = Partition(arr, beg, end, mainMed)
    print("q = {}".format(q))
    k = q - beg + 1
    if k == i:
        return arr[q]
    elif i > k:
        return Select(arr, q + 1, end, i - k)
    else:
        return Select(arr, beg, q - 1, i)


'''numList = []
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
while True:
    ordNum = input("Enter the number of the order statistic: ")
    if ordNum == 's':
        break
    ord = Select(numList, 0, len(numList) - 1, int(ordNum))
    print("ord = {}".format(ord))'''

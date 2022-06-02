import time

def RadixSort(arr, d):
    n = len(arr)
    for m in range(d - 1, -1, -1):
        B = list()
        C = list()
        for i in range(0, 10):
            C.append(0)
        for j in range(0, n):
            ind = int(str(arr[j])[m])
            print("j = {}; arr[{}] = {}".format(j, j, arr[j]))
            print("i = {}; ind = {}".format(i, ind))
            C[ind] += 1
            B.append(0)
        print("C = {}".format(C))
        for i in range(1, 10):
            C[i] += C[i - 1]
        print("C = {}".format(C))
        for l in range(n - 1, -1, -1):
            print("l = {} arr[{}] = {} C[{}] = {} ".format(l, l, arr[l], arr[l], C[int(str(arr[l])[m])]))
            B[C[int(str(arr[l])[m])] - 1] = arr[l]
            C[int(str(arr[l])[m])] -= 1
        print("B = {}".format(B))
        arr = B
    return arr

def VarSizeSort(arr):
    n = len(arr)
    szList = list()
    resList = list()
    for i in range(0, n):
        szList.append(list())
    for i in range(0, n):
        szList[len(str(arr[i]))].append(arr[i])
    print("szList = {}".format(szList))
    for col in szList:
        if len(col) > 0:
            col = RadixSort(col, len(str(col[0])))
            print("col = {}".format(col))
            resList.extend(col)
    return resList

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
clock = time.time()
numList = VarSizeSort(numList)
print("time = {}".format(time.time() - clock))
print("sorted list = {}".format(numList))

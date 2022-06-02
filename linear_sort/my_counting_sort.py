def MyCountingSort(arr):
    countList = list()
    n = len(arr)
    for i in range(0, 10):
        countList.append(0)
    for i in range(0, n):
        countList[arr[i]] += 1
    print("c = {}".format(countList))
    j = 9
    i = n - 1
    while i >= 0:
        if countList[j] == 0:
            j -= 1
            continue
        print("arr[{}] = {}; c[{}] = {}".format(i, arr[i], j, arr[j]))
        arr[i] = j
        countList[j] -= 1
        i -= 1
    print("sorted list = {}".format(arr))

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
MyCountingSort(numList)

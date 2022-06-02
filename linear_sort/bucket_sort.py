def BucketSort(arr):
    n = len(arr)
    B = list()
    for i in range(0, 10):
        B.append(list())
    print("B = {}".format(B))
    for j in range(0, n):
        B[int(n*arr[j])].append(arr[j])
    print("B = {}".format(B))
    for col in B:
        for i in range(1, len(col)):
            key = col[i]
            j = i - 1
            while j >= 0 and col[j] >= key:
                col[j + 1] = col[j]
                j -= 1
            col[j + 1] = key
        print("list = {}".format(col))
    for k in range(1, len(B)):
        B[0].extend(B[k])
    return B[0]

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
numList = BucketSort(numList)
print("sorted list = {}".format(numList))

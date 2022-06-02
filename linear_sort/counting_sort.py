import time

def CountingSort(arr, k = 10):
    B = list()
    C = list()
    n = len(arr)
    for i in range(0, k):
        C.append(0)
    for j in range(0, n):
        C[arr[j]] += 1
        B.append(0)
    print("C = {}".format(C))
    for i in range(1, k):
        C[i] += C[i - 1]
    print("C = {}".format(C))
    for l in range(n - 1, -1, -1):
        print("l = {} arr[{}] = {} C[{}] = {} ".format(l, l, arr[l], arr[l], C[arr[l]]))
        B[C[arr[l]] - 1] = arr[l]
        C[arr[l]] -= 1
    print("B = {}".format(B))
    return B

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
numList = CountingSort(numList)
print("time = {}".format(time.time() - clock))
print("sorted list = {}".format(numList))

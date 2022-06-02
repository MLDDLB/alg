import time

def BinarySort(arr):
    n = len(arr)
    count = 0
    for i in range(0, n):
        if arr[i - count] == 1:
            arr.append(arr[i - count])
            arr.pop(i - count)
            count += 1


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
BinarySort(numList)
print("time = {}".format(time.time() - clock))
print("sorted list = {}".format(numList))

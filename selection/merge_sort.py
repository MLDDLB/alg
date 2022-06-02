def Merge(arr, p, q, r):
    L = [i for i in arr[p:q+1]]
    print("L = {}".format(L))
    R = [j for j in arr[q+1:r+1]]
    print("R = {}".format(R))
    n1 = len(L)
    n2 = len(R)
    i = 0
    j = 0
    for k in range(p, r+1):
        try:
            if L[i] <= R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
        except:
            if k == r:
                break
            elif i >= n1:
                arr[k] = R[j]
                j += 1
            elif j >= n2:
                arr[k] = L[i]
                i += 1
    return()

def MergeSort(arr, p, r):
    if p < r:
        q = int((r+p)/2)
        print(" p = {} r = {} q = {}".format(p,r,q))
        MergeSort(arr, p, q)
        print("finished 1")
        MergeSort(arr, q+1, r)
        print("finished 2")
        Merge(arr, p, q, r)
        print("list: {}".format(arr))
    return()

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
print(numList)
MergeSort(numList, 0, len(numList))
print(numList)'''

'''arr = [1, 2, 3, 4]
test = [i for i in arr[1:3]]
print(test)'''

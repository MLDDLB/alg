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
print("The resulting collection: {}".format(numList))
n = len(numList)
for i in range(0, n):                                   
    for j in range(n - 1, i, -1):
        print("j = {}".format(j))
        if numList[j] < numList[j - 1]:
            key = numList[j]
            numList[j] = numList[j - 1]
            numList[j - 1] = key
print("Sorted collection: {}".format(numList))

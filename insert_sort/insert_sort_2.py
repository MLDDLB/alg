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
for i in range(1, n):
    key = numList[i]
    j = i - 1
    while j >= 0 and numList[j] <= key:
        numList[j+1] = numList[j]
        j -= 1
    numList[j + 1] = key
print("Sorted collection: {}".format(numList))

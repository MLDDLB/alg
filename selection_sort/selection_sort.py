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
print(numList)
n = len(numList)
for j in range(0, n):
    min = numList[j]
    index = j
    for i in range(j, n):
        if numList[i] < min:
            min = numList[i]
            index = i
    numList[index] = numList[j]
    numList[j] = min
print(numList)

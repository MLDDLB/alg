import random

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
for i in range(0, n):
    buff = numList[i]
    ind = random.randrange(i, n)
    numList[i] = numList[ind]
    numList[ind] = buff
print("list = {}".format(numList))

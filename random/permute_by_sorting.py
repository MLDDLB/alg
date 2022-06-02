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
prList = list()
randEnd = n**3
for i in range(0, n):
    prList.append(random.randrange(0, randEnd))
print("priority list = {}".format(prList))
key = None
for i in range(0, n):
    key = prList[i]
    value = numList[i]
    j = i - 1
    while j >= 0 and prList[j] <= key:
        numList[j + 1] = numList[j]
        prList[j + 1] = prList[j]
        j -= 1
    prList[j + 1] = key
    numList[j + 1] = value
print("sorted priority list = {} \n sorted numlist = {}".format(prList, numList))

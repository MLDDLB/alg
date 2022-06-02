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
indexList = list()
x = int(input("Enter the number you're searching for: "))
counter = 0
while True:
    ind = random.randrange(0, n)
    if numList[ind] == x:
        print("Found at: {}".format(ind))
        break
    elif indexList.count(ind) == 0:
        indexList.append(ind)
    elif len(indexList) == n:
        print("Not found")
        break
    counter += 1
print("counter = {}".format(counter))

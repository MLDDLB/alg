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
v = int(input("Enter the number that will be searched for: "))
index = None
for i in numList:
    if i == v:
        index = numList.index(i)
        break
    continue
print("Index: {}".format(index))

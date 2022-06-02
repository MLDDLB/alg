numList = []
while True:
    try:
        num = int(input("Enter a coefficient: "))
    except:
        print("Enter an integer number")
        continue
    if num == -1:
        break
    numList.append(num)
print("list of coefficients: {}".format(numList))
x = int(input("Enter the value of x: "))
n = len(numList)
res = 0
for i in range(0, n):
    res = res + numList[i]*pow(x, i)
print("Polynome equals: {}".format(res))

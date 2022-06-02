def FindMaximumSubarray(arr):
    max_low = None
    max_high = None
    max_sum = float("-inf")
    for i in range(0, len(arr)):
        sum = 0
        for j in range(i, len(arr)):
            sum = sum + arr[j]
            if sum > max_sum:
                max_low = i
                max_high = j
                max_sum = sum
    return(max_low, max_high, max_sum)

def main():
    numList = list()
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
    maxSub = FindMaximumSubarray(numList)
    print("low = {}, high = {}, sum = {}".format(maxSub[0], maxSub[1], maxSub[2]))

if __name__ == "__main__":
    main()

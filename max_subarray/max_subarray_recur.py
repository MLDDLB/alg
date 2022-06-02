def FindMaxCrossingSubarray(arr, low, high, mid):
    left_sum = float("-inf")
    sum = 0
    max_left = None
    for i in range(mid, low - 1, -1):
        sum = sum + arr[i]
        if sum > left_sum:
            left_sum = sum
            max_left = i
    right_sum = float("-inf")
    sum = 0
    max_right = None
    for j in range(mid + 1, high):
        sum = sum + arr[j]
        if sum > right_sum:
            right_sum = sum
            max_right = j
    return((max_left, max_right, left_sum + right_sum))

def FindMaximumSubarray(arr, low, high):
    if low == high:
        return(low, high, arr[low])
    else:
        print("recur")
        mid = int((high + low)/2)
        (left_low, left_high, left_sum) = FindMaximumSubarray(arr, low, mid)
        (right_low, right_high, right_sum) = FindMaximumSubarray(arr, mid + 1, high)
        (cross_low, cross_high, cross_sum) = FindMaxCrossingSubarray(arr, low, high, mid)
        if left_sum > right_sum and left_sum > cross_sum:
            return(left_low, left_high, left_sum)
        elif right_sum > left_sum and right_sum > cross_sum:
            return(right_low, right_high, right_sum)
        else:
            return(cross_low, cross_high, cross_sum)

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
    maxSub = FindMaximumSubarray(numList, 0, len(numList) - 1)
    print("low = {}, high = {}, sum = {}".format(maxSub[0], maxSub[1], maxSub[2]))

if __name__ == "__main__":
    main()

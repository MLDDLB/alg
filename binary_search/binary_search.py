from merge_sort import MergeSort, Merge

def BinarySearch(arr, num, begining, end):
    if begining < end:
        index = None
        q = int((begining + end)/2)
        print("beg = {} end = {} q = {}".format(begining, end, q))
        if num == arr[q]:
            print("index = {} arr[ind] = {}".format(q, arr[q]))
            index = q
        elif num > arr[q]:
            print(">")
            index = BinarySearch(arr, num, q, end)
        elif num < arr[q]:
            print("<")
            index = BinarySearch(arr, num, begining, q)
        print("q = {}".format(q))
        return(index)

arr = list()
while True:
    try:
        num = int(input("Enter a numer: "))
    except:
        print("You must enter a valid number!")
        continue
    if num == -1:
        break
    arr.append(num)
MergeSort(arr, 0, len(arr) - 1)
print("list: {}".format(arr))
dnum = int(input("Enter a number you want to find: "))
ind = BinarySearch(arr, dnum, 0, len(arr) - 1)
print("Index of the number you've searched for is: {}".format(ind))

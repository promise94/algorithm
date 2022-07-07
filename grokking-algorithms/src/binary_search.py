def binarySearch(item, arr):
    low = 0
    m = len(arr) - 1

    while True:
        mid = (low + m) // 2
        print('mid: ', mid)
        if arr[mid] < item:
            low = mid + 1
        elif arr[mid] > item:
            m = mid - 1
        else:
            return mid


print(binarySearch(6, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))

# O(n * log n)
def quick_sort(arr):
    if len(arr) < 2:
        return arr
    mid = len(arr) // 2
    base = arr[mid]
    less = [i for i in arr if i < base]
    greater = [i for i in arr if i > base]
    equal = [i for i in arr if i == base]
    return quick_sort(less) + equal + quick_sort(greater)


print(quick_sort([2, 1, 3, 3, 4, 2, 6, 7, 1, 9]))
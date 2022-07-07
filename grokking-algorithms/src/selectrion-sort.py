def find_smallest(arr):
    smallest = arr[0]
    sub = 0
    for i in range(1, len(arr)):
        if arr[i] < smallest:
            smallest = arr[i]
            sub = i
    return sub, smallest


def selection_sort(arr):
    new_arr = []
    # while len(arr):
    for i in range(len(arr)):
        sub, smallest = find_smallest(arr)
        new_arr.append(arr.pop(sub))
        print(new_arr, arr)

    return new_arr


print(selection_sort([2, 3, 32, 2, 45, 1, 90, 4, 0]))

def bubbleSort(arr: list):
    for i in range(len(arr) - 1):
        for j in range(len(arr) - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr


print(bubbleSort([1, 5, 3, 7, 6, 8, 2, 4]))

def selectionSort(arr: list):
    for i in range(len(arr)):
        minimum = i

        for j in range(i+1, len(arr)):
            if arr[j] < arr[minimum]:
                minimum = j

        arr[minimum], arr[i] = arr[i], arr[minimum]
    return arr


print(selectionSort([9, 1, 5, 3, 7,10,19,18,26, 4, 2, 8, 6]))

def linearSearch(arr: list, key: int):
    for i in range(len(arr)):
        if arr[i] == key:
            return i
    return -1


print(linearSearch([1, 2, 3, 4, 5], 4))

def binarySearch(arr: list, key: int):
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2
        if arr[mid] < key:
            low = mid+1
        elif arr[mid] > key:
            high = mid-1
        else:
            return f'Element {arr[mid]} for at index {mid}'
    return -1


print(binarySearch([1,2,3,4,5],4))



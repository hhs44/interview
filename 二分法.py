def binarySearch(arr, left, right, x):
    while left <= right:
        mid = int(left + (right - left) / 2)
        if arr[mid] == x:
            print(f'found{x} in {mid}')
            return mid
        elif arr[mid] < x:
            left = mid + 1
        elif x < arr[mid]:
            right = mid - 1
    return -1

def recursion_binary_search(array, target, start, end):
    if start > end:
        return None
    mid = (start + end) // 2

    if array[mid] == target:
        return mid
    elif array[mid] > target:
        return recursion_binary_search(array, start, mid - 1)
    else:
        return recursion_binary_search(array, mid + 1, end)

def loop_binary_search(array, target, start, end):
    while start < end:
        mid = (start + end) // 2
        if array[mid] == target:
            return mid
        elif array[mid] > target:
            end = mid - 1
        else:
            start = mid + 1
    return None
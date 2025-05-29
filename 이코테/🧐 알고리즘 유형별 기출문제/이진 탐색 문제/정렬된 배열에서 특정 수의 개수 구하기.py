import bisect

n, x = map(int, input().split())
sequence = list(map(int, input().split()))

def solution1():
    left = bisect.bisect_left(sequence, x)
    right = bisect.bisect_right(sequence, x)

    answer = right - left
    print(answer if answer > 0 else -1)

def solution2():
    left = first(sequence, x, 0, n - 1)
    right = last(sequence, x, 0, n - 1)
    answer = right - left + 1
    if left != -1:
        print(answer)
    else:
        print(-1)
    return

def first(arr, x, start, end):
    if start > end:
        return -1
    
    mid = (start + end) // 2
    if (mid == 0 or x > arr[mid - 1]) and (arr[mid] == x):
        return mid
    elif arr[mid] >= x:
        return first(arr, x, start, mid - 1)
    else:
        return first(arr, x, mid + 1, end)
    

def last(arr, x, start, end):
    if start > end:
        return -1
    
    mid = (start + end) // 2
    if (mid == n - 1 or x < arr[mid + 1]) and (arr[mid] == x):
        return mid
    elif arr[mid] > x:
        return last(arr, x, start, mid - 1)
    else:
        return last(arr, x, mid + 1, end)

solution1()
solution2()
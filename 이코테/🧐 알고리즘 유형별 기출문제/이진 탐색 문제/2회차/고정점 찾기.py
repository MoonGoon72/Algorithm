n = int(input())
arr = list(map(int, input().split()))

def binary_search(start, end, arr):
    if start > end:
        return None
    
    mid = (start + end) // 2
    if arr[mid] == mid:
        return mid
    elif arr[mid] > mid:
        return binary_search(start, end - 1, arr)
    else:
        return binary_search(mid + 1, end, arr)

answer = binary_search(0, n - 1, arr)
if answer == None:
    print(-1)
else:
    print(answer)
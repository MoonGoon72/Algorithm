import sys
input = sys.stdin.readline

n, c = map(int, input().split())
arr = []
for _ in range(n):
    arr.append(int(input()))
arr.sort()
gap = 0

def binary_search(start, end, arr):
    global gap
    if start > end:
        return
    mid = (start + end) // 2
    result = [arr[0]]
    for i in range(1, n):
        if arr[i] - result[-1] >= mid:
            result.append(arr[i])
    
    if len(result) < c:
        return binary_search(start, mid - 1, arr)
    else:
        gap = mid
        return binary_search(mid + 1, end, arr)

max_gap = arr[n - 1] - arr[0]
min_gap = 1

binary_search(min_gap, max_gap, arr)
print(gap)
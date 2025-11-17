import sys
input = sys.stdin.readline

k, n = map(int, input().split())
data = list(int(input()) for _ in range(k))

def calc(arr, length):
    count = 0
    for l in arr:
        count += l // length
    return count

def binary_search(start, end):
    result = 0
    while start <= end:
        mid = (start + end) // 2
        value = calc(data, mid)
        if value >= n:
            start = mid + 1
            result = mid
        else:
            end = mid - 1
    return result

answer = binary_search(1, max(data))
print(answer)
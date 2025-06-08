import sys
input = sys.stdin.readline

n = int(input())
data = list(map(int, input().split()))

def dp_solution():
    dp = [1] * n

    for i in range(n):
        for j in range(0, i):
            if data[i] < data[j]:
                dp[i] = max(dp[i], dp[j] + 1)

    answer = n - max(dp)
    print(answer)

def binary_search(arr, val):
    start, end = 0, len(arr) - 1
    while start < end:
        mid = (start + end) // 2
        if arr[mid] <= val:
            end = mid
        else:
            start = mid + 1
    return start

def binary_search_solution():
    lds = []
    
    for i in range(n):
        val = data[i]
        if not lds or lds[-1] > val:
            lds.append(val)
        else:
            pos = binary_search(lds, val)
            lds[pos] = val
    answer = n - len(lds)
    print(answer)

binary_search_solution()
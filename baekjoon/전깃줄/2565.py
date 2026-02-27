import sys
input = sys.stdin.readline

n = int(input())
arr = []
for _ in range(n):
    a, b = map(int, input().split())
    arr.append((a, b))
arr.sort(key=lambda x: x[0])

dp = [1] * (n+1)
def lis(arr):
    for i in range(n):
        for j in range(i):
            if arr[j][1] < arr[i][1]:
                dp[i] = max(dp[i], dp[j]+1)
    print(n - max(dp))

lis(arr)
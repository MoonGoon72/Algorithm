import sys
input = sys.stdin.readline

n = int(input())
arr = []
for i in range(n):
    arr.append(list(map(int, input().split())) + [0] * (n - i - 1))

dp = []
for _ in range(n):
    dp.append([0] * n)

dp[0][0] = arr[0][0]
for i in range(n - 1):
    for j in range(n - 1):
        dp[i + 1][j] = max(dp[i + 1][j], dp[i][j] + arr[i + 1][j])
        dp[i + 1][j + 1] = max(dp[i + 1][j + 1], dp[i][j] + arr[i + 1][j + 1])
    
print(max(dp[n - 1]))

import sys
input = sys.stdin.readline

n = int(input())
arr = [0] + list(map(int, input().split()))
l = len(arr)
dp = [0] * (n+1)

for i in range(1, l):
    dp[i] = arr[i]

for i in range(2, n+1):
    for j in range(1, l):
        if i-j < 0:
            break
        dp[i] = max(dp[i], dp[i-j] + arr[j])
print(dp[n])
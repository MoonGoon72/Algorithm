import sys
input = sys.stdin.readline

n = int(input())
dp = [[0] * 10 for _ in range(n+1)]
for i in range(10):
    dp[1][i] = 1

for i in range(2, n+1):
    for j in range(10):
        for k in range(10):
            if j > k: continue
            dp[i][j] += dp[i-1][k] % 10_007

print(sum(dp[n]) % 10_007)
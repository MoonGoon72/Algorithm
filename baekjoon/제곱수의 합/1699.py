n = int(input())

inf = int(1e9)
dp = [0] + [inf] * n

for i in range(1, n+1):
    for j in range(1, int(i ** 0.5) + 1):
        dp[i] = min(dp[i], dp[i - j * j] + 1)
print(dp[n])
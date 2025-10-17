import sys
input = sys.stdin.readline

n, k = map(int, input().split())
coins = list(int(input()) for _ in range(n))
coins.sort()

dp = [0] * (k + 1)
dp[0] = 1

for coin in coins:
    for i in range(1, k + 1):
        if i - coin < 0:
            continue
        dp[i] += dp[i - coin]
print(dp[k])
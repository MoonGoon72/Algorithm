n = int(input())

if n < 2:
    print(0)
    exit(0)
dp = [0] * (n+1)
dp[0] = 1
dp[2] = 3

for k in range(4, n+1, 2):
    dp[k] += dp[k-2] * 3
    for i in range(0, k-2, 2):
        dp[k] += 2 * dp[i]
print(dp[n] if n % 2 == 0 else 0)
n, k = map(int, input().split())

mod = 10_007
dp = [1] * (n+1)

for i in range(2, n+1):
    dp[i] = dp[i-1] * i
answer = (dp[n] // (dp[k]*dp[n-k])) % mod
print(answer)
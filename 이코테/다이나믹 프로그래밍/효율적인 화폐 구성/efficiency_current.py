import sys
input = sys.stdin.readline

n, m = map(int, input().split())
currents = list(int(input()) for _ in range(n))
INF = 10001
dp = [0] + [INF] * 10000 # 0은 아무것도 안하면 되니까 0으로 가능

for current in currents:
    dp[current] = 1

for current in currents:
    for j in range(current, m + 1):
        if dp[j] == INF:
            continue
        dp[j] = min(dp[j], dp[j - current] + 1)

print(dp[m] if dp[m] != INF else -1)
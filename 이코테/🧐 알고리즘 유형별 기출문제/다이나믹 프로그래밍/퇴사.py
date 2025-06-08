import sys
input = sys.stdin.readline

n = int(input())
data = [(0, 0)]

for _ in range(n):
    need_days, cost = map(int, input().split())
    data.append((need_days, cost))

dp = [0] * (n + 1)

for i in range(1, n + 1):
    need_days, cost = data[i]
    next_days = need_days - 1 + i
    if next_days <= n:
        dp[next_days] = max(dp[next_days], max(dp[:i]) + cost)

print(max(dp))
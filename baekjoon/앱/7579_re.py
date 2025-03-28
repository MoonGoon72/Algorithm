import sys
input = sys.stdin.readline

n, m = map(int, input().split())
mems = [0] + list(map(int, input().split()))
costs = [0] + list(map(int, input().split()))

max_cost = sum(costs)
dp = [[0] * (max_cost + 1) for _ in range(n + 1)]

result = max_cost

for i in range(1, n + 1):
    mem, cost = mems[i], costs[i]
    for j in range(max_cost + 1):
        if j < cost:
            dp[i][j] = dp[i - 1][j]
            continue

        dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - cost] + mem)
        if dp[i][j] >= m:
            result = min(result, j)

print(result)
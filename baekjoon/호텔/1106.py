import sys
input = sys.stdin.readline

inf = int(1e9)
c, n = map(int, input().split())
data = [tuple(map(int, input().split())) for _ in range(n)]

dp = [inf] * (2000)
dp[0] = 0
for i in range(c):
    for cost, customer in data:
        dp[i + customer] = min(dp[i + customer], dp[i] + cost)

answer = min(dp[c:])
print(answer)

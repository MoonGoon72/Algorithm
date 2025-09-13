import sys
input = sys.stdin.readline

n = int(input())
t, p = [], []
dp = [0] * (n + 1)
max_value = 0

for _ in range(n):
    a, b = map(int, input().split())
    t.append(a)
    p.append(b)

for i in range(n - 1, -1, -1):
    time = i + t[i]
    if time > n:
        dp[i] = max_value
    else:
        dp[i] = max(p[i] + dp[time], max_value)
        max_value = max(max_value, dp[i])

print(max_value)

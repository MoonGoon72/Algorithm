import sys
input = sys.stdin.readline

n = int(input())
data = []
dp = []
i = 4

for _ in range(n):
    line = list(map(int, input().split())) + [0] * i
    data.append(line)
    dp.append(line)
    i -= 1

for i in range(1, n):
    # 위, 왼쪽 중 하나.
    for j in range(i + 1):
        if j == 0:
            left_up = 0
        else:
            left_up = dp[i - 1][j - 1]
        if j >= len(dp[i - 1]):
            up = 0
        else:
            up = dp[i - 1][j]

        dp[i][j] += max(left_up, up)

print(max(dp[n - 1]))
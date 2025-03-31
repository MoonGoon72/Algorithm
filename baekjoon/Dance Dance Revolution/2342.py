import sys
input = sys.stdin.readline
INF = int(1e9)

def move_cost(from_pos, to_pos):
    if from_pos == 0:
        return 2
    elif from_pos == to_pos:
        return 1
    elif abs(from_pos - to_pos) == 2:
        return 4
    else:
        return 3

orders = list(map(int, input().split()))
orders.pop()
length = len(orders)
dp = [[[INF] * 5 for _ in range(5)] for _ in range(length + 1)]
dp[0][0][0] = 0

for i in range(length):
    next = orders[i]
    for l in range(5):
        for r in range(5):
            if dp[i][l][r] == INF:
                continue
            dp[i + 1][next][r] = min(dp[i + 1][next][r], dp[i][l][r] + move_cost(l, next))
            dp[i + 1][l][next] = min(dp[i + 1][l][next], dp[i][l][r] + move_cost(r, next))

result = INF
for l in range(5):
    for r in range(5):
        result = min(result, dp[length][l][r])

print(result)
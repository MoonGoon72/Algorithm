import sys
input = sys.stdin.readline
INF = int(1e9)

def move_cost(a, b):
    if a == 0:
        return 2
    elif a == b:
        return 1
    elif abs(a - b) == 2:
        return 4
    else:
        return 3
    
orders = list(map(int, input().split()))
orders.pop()
n = len(orders)
dp = [[[INF] * (5) for _ in range(5)] for _ in range(n + 1)]
dp[0][0][0] = 0

for i in range(n):
    next_move = orders[i]
    for l in range(5):
        for r in range(5):
            dp[i + 1][next_move][r] = min(dp[i + 1][next_move][r], dp[i][l][r] + move_cost(l, next_move))
            dp[i + 1][l][next_move] = min(dp[i + 1][l][next_move], dp[i][l][r] + move_cost(r, next_move))

answer = INF
for l in range(5):
    for r in range(5):
        answer = min(answer, dp[n][l][r])
print(answer)
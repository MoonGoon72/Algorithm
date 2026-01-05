import sys
input = sys.stdin.readline

dy = [0, 1, 1]
dx = [1, 0, 1]

# 가로 세로 대각선
directions = [[0, 2], [1, 2], [0, 1, 2]]

n = int(input())
board = []
board.append([1] * (n + 2))
for _ in range(n):
    line = list(map(int, input().split()))
    board.append([1] + line + [1])
board.append([1] * (n + 2))

dp = list([[0, 0, 0] for _ in range(n + 2)] for _ in range(n + 2))

pipe = [(1, 1), (1, 2), 0]
dp[1][2][0] = 1

for y in range(1, n + 1):
    for x in range(1, n + 1):
        if board[y][x] == 1:
            continue

        if x - 1 >= 1:
            dp[y][x][0] += dp[y][x-1][0] + dp[y][x-1][2]
        if y - 1 >= 1:
            dp[y][x][1] += dp[y-1][x][1] + dp[y-1][x][2]
        if y - 1 >= 1 and x - 1 >= 1 and board[y-1][x] == 0 and board[y][x-1] == 0:
            dp[y][x][2] = dp[y-1][x-1][0] + dp[y-1][x-1][1] + dp[y-1][x-1][2]

print(sum(dp[n][n]))
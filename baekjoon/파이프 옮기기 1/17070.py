import sys
input = sys.stdin.readline

n = int(input())
graph = list(list(map(int, input().split())) for _ in range(n))

dp = [[[0] * 3 for _ in range(n)] for _ in range(n)]
dp[0][1][0] = 1

state = 0  # 0 = 가로, 1 = 세로, 2 = 대각선
answer = 0
right = (0, 1)
down = (1, 0)
diagnal = (1, 1)

def check(y, x):
    return 0 <= y < n and 0 <= x < n and graph[y][x] != 1

def move(state, y, x):
    result = []
    if state == 0:
        ny = y + right[0]
        nx = x + right[1]
        if check(ny, nx): result.append((state, ny, nx))
        ny, nx = y + diagnal[0], x + diagnal[1]
        if check(ny, nx) and check(ny - 1, nx) and check(ny, nx - 1): result.append((2, ny, nx))
    elif state == 1:
        ny = y + down[0]
        nx = x + down[1]
        if check(ny, nx): result.append((state, ny, nx))
        ny, nx = y + diagnal[0], x + diagnal[1]
        if check(ny, nx) and check(ny - 1, nx) and check(ny, nx - 1): result.append((2, ny, nx))
    elif state == 2:
        ny, nx = y + right[0], x + right[1]
        if check(ny, nx): result.append((0, ny, nx))
        ny, nx = y + down[0], x + down[1]
        if check(ny, nx): result.append((1, ny, nx))
        ny, nx = y + diagnal[0], x + diagnal[1]
        if check(ny, nx) and check(ny - 1, nx) and check(ny, nx - 1): result.append((state, ny, nx))
    return result

def dfs():
    global answer
    stack = []
    stack.append((0, 0, 1))

    while stack:
        nowState, y, x = stack.pop()
        if y == n - 1 and x == n - 1: 
            answer += 1
            continue
        stack += move(nowState, y, x)
    return

def solution():
    for y in range(n):
        for x in range(n):
            if graph[y][x] == 1: continue

            # 가로
            if x > 0:
                dp[y][x][0] += dp[y][x-1][0] + dp[y][x-1][2]
            # 세로
            if y > 0:
                dp[y][x][1] += dp[y-1][x][1] + dp[y-1][x][2]
            # 대각선
            if x > 0 and x > 0 and graph[y-1][x] != 1 and graph[y][x-1] != 1:
                dp[y][x][2] += dp[y-1][x-1][0] + dp[y-1][x-1][1] + dp[y-1][x-1][2]
    return

# dfs()
# print(answer)
solution()
print(sum(dp[n-1][n-1]))
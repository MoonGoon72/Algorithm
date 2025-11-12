import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]

m, n = map(int, input().split())
graph = list(list(map(int, input().split())) for _ in range(m))
dp = [[-1] * n for _ in range(m)]

def check(y, x):
    return 0 <= y < m and 0 <= x < n

def dfs(y, x):
    if (y, x) == (m - 1, n - 1): return 1
    
    if dp[y][x] != -1: return dp[y][x]
    dp[y][x] = 0

    for d in range(4):
        ny, nx = y + dy[d], x + dx[d]
        if not check(ny, nx) or graph[ny][nx] >= graph[y][x]:
            continue
        
        if dp[ny][nx] != -1:
            dp[y][x] += dp[ny][nx]
        else:
            dp[y][x] += dfs(ny, nx)
    return dp[y][x]

answer = dfs(0, 0)
print(answer)

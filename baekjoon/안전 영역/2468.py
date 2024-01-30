import sys
from collections import deque

input = sys.stdin.readline
n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]
visited = [[False for _ in range(n)] for _ in range(n)]
max_value = max(map(max, graph))
result = 1

dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]

def check(y, x):
    return 0 <= y < n and 0 <= x < n

def bfs(row, col, rain_depth):
    global visited
    global graph
    queue = deque()
    queue.append((row, col))
    while queue:
        y, x = queue.popleft()
        visited[y][x] = True
        for i in range(4):
            ny, nx = y + dy[i], x + dx[i]
            if check(ny, nx):
                if graph[ny][nx] > rain_depth and not visited[ny][nx]:
                    queue.append((ny, nx))
                    visited[ny][nx] = True

for i in range(max_value):
    safe_area = 0
    for row in range(n):
        for col in range(n):
            if graph[row][col] > i and not visited[row][col]:
                bfs(row, col, i)
                safe_area += 1
    result = max(result, safe_area)
    visited = [[False for _ in range(n)] for _ in range(n)]
print(result)

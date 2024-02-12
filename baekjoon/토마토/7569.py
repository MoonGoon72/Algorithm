from collections import deque
import sys
input = sys.stdin.readline

m, n, h = map(int, input().split()) # col, row, height

dx = [-1, 1 ,0, 0, 0, 0]
dy = [0, 0, -1 ,1, 0, 0]
dz = [0, 0, 0, 0, -1, 1]


graph = []

for _ in range(h):
    box = []
    for _ in range(n):
        arr = list(map(int, input().split()))
        box.append(arr)
    graph.append(box)

queue = deque()

# 처음 익은 토마토의 위치
for height in range(h):
    for row in range(n):
        for col in range(m):
            if graph[height][row][col] == 1: queue.append((height, row, col))

def check(height, row, col):
    return 0 <= row < n and 0 <= col < m and 0 <= height < h

def bfs():
    while queue:
        z, y, x = queue.popleft()
        for i in range(6):
            nz = z + dz[i]
            ny = y + dy[i]
            nx = x + dx[i]
            if check(nz, ny, nx):
                if graph[nz][ny][nx] == 0:
                    graph[nz][ny][nx] = graph[z][y][x] + 1
                    queue.append((nz, ny, nx))

bfs()
result = 0
for i in range(h):
    for j in range(n):
        for k in range(m):
            if graph[i][j][k] == 0:
                print("-1")
                exit(0)
        result = max(result, max(graph[i][j]))
print(result - 1)
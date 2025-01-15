from collections import deque
import sys
input = sys.stdin.readline

r, c = map(int, input().split())
graph = list(list(map(int, input().strip())) for _ in range(r))
visited = [[False] * c for _ in range(r)]

dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]

def check(y, x):
    return 0 <= y < r and 0 <= x < c

def bfs(y, x):
    queue = deque()
    queue.append((y, x))
    visited[y][x] = True

    while queue:
        y, x = queue.popleft()
        for i in range(4):
            ny, nx = y + dy[i], x + dx[i]
            if check(ny, nx) and graph[ny][nx] != 0 and not visited[ny][nx]:
                graph[ny][nx] = graph[y][x] + 1
                visited[ny][nx] = True
                queue.append((ny, nx))
    print(graph[r-1][c-1])
    return

bfs(0, 0)
"""
5 6
101010
111111
000001
111111
111111
"""
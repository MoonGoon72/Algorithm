import queue
import sys
from collections import deque
input = sys.stdin.readline

N, M = map(int, input().split())
graph = [list(map(int,input().rstrip())) for _ in range(N)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x,y):
    queue = deque()
    queue.append((x,y))

    nx = 0
    ny = 0

    while queue:
        x, y = queue.popleft()
        
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]

            if (nx >=0 and ny >=0 and nx < N and ny < M and graph[nx][ny] == 1):
                graph[nx][ny] = graph[x][y] + 1
                queue.append((nx,ny))
    return graph[N-1][M-1]
print(bfs(0,0))

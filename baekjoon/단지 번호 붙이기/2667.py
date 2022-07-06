from operator import eq
import sys
from collections import deque
input = sys.stdin.readline

N = int(input())
graph = [list(map(int, input().rstrip())) for _ in range(N)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x,y):
    queue = deque()
    queue.append((x,y))
    graph[x][y] = 0
    count = 0

    while queue:
        x, y = queue.popleft()
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

        if (nx >= 0 and ny >= 0 and nx < N and ny < N and graph[nx][ny] == 1):
            graph[nx][ny] = 0
            queue.append((x,y))
            count += 1
    return count

print(bfs(0,0))
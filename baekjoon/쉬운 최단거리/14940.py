import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split()) # n = row, m = col
graph = [list(map(int, input().split())) for _ in range(n)]
isVisited = [[False for _ in range(m)] for _ in range(n)]

dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]

def searchStart():
    for row in range(n):
        for col in range(m):
            if graph[row][col] == 2:
                return (row, col)

def check(y, x):
    return 0 <= y < n and 0 <= x < m

def bfs(y, x):
    graph[start[0]][start[1]] = 0
    isVisited[start[0]][start[1]] = True
    queue = deque()
    queue.append((y, x))
    while queue:
        now = queue.popleft()
        for i in range(4):
            ny = now[0] + dy[i]
            nx = now[1] + dx[i]
            if check(ny, nx):
                if isVisited[ny][nx]: continue
                if graph[ny][nx] == 1:
                    graph[ny][nx] += graph[now[0]][now[1]]
                    queue.append((ny, nx))
                    isVisited[ny][nx] = True
                elif graph[ny][nx] == 0:
                    isVisited[ny][nx] = True
                    continue
                else:
                    graph[ny][nx] = min(graph[ny][nx], graph[now[0]][now[1]] + 1)
                    isVisited[ny][nx] = True

def findUnreachableLocations():
    for row in range(n):
        for col in range(m):
            if not isVisited[row][col] and graph[row][col] == 1: graph[row][col] = -1

start = searchStart()
bfs(start[0], start[1])
findUnreachableLocations()

for row in range(n):
    for col in range(m):
        print(graph[row][col], end=' ')
    print()

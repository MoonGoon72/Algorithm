from collections import deque
import sys
input = sys.stdin.readline

inf = int(1e9)
dy = [-1, 0, 1, 0]
dx = [0, -1, 0, 1]

n = int(input())
graph = []
now_size = 2
now_y, now_x = 0, 0
for i in range(n):
    line = list(map(int, input().split()))
    for j in range(n):
        if line[j] == 9:
            now_y, now_x = i, j
            line[j] = 0
    graph.append(line)

def check(y, x):
    return 0 <= y < n and 0 <= x < n

def bfs():
    dist = [[-1] * n for _ in range(n)]
    queue = deque([(now_y, now_x)])
    dist[now_y][now_x] = 0

    while queue:
        y, x = queue.popleft()
        for i in range(4):
            ny, nx = y + dy[i], x + dx[i]
            if check(ny, nx):
                if dist[ny][nx] == -1 and graph[ny][nx] <= now_size:
                    dist[ny][nx] = dist[y][x] + 1
                    queue.append((ny, nx))
    return dist

def find(dist):
    y, x = 0, 0
    min_dist = inf
    for i in range(n):
        for j in range(n):
            if dist[i][j] != -1 and 1 <= graph[i][j] and graph[i][j] < now_size:
                if dist[i][j] < min_dist:
                    min_dist = dist[i][j]
                    y, x = i, j
    if min_dist == inf:
        return None
    else:
        return y, x, min_dist
    
result = 0
ate = 0

while True:
    dist = bfs()
    value = find(dist)
    if value == None:
        print(result)
        break
    else:
        y, x, min_dist = value
        result += min_dist
        now_y, now_x = y, x
        graph[y][x] = 0
        ate += 1
        if ate >= now_size:
            now_size += 1
            ate = 0

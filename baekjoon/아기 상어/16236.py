from collections import deque
import sys
input = sys.stdin.readline

INF = int(1e9)
dy = [-1, 0, 0, 1]
dx = [0, -1, 1, 0]

n = int(input())
graph = []
sy, sx = 0, 0

for i in range(n):
    line = list(map(int, input().split()))
    for j in range(n):
        if line[j] == 9:
            sy, sx = i, j
            line[j] = 0
    graph.append(line)

def check(y, x):
    return 0 <= y < n and 0 <= x < n

def find(graph, sy, sx, shark):
    visited = [[False] * n for _ in range(n)]
    visited[sy][sx] = True
    queue = deque([(sy, sx, 0)])
    candidates = []
    min_dist = INF
    while queue:
        y, x, d = queue.popleft()

        if min_dist is not None and d > min_dist:
            break

        if graph[y][x] != 0 and graph[y][x] < shark:
            candidates.append((y, x, d))
            min_dist = d
            continue

        for i in range(4):
            ny, nx = y + dy[i], x + dx[i]
            if check(ny, nx) and not visited[ny][nx] and graph[ny][nx] <= shark:
                visited[ny][nx] = True
                queue.append((ny, nx, d + 1))
    if candidates:
        candidates.sort()
        cy, cx, cd = candidates[0]
        return (cy, cx, cd)

    return None

def bfs(graph, sy, sx):
    shark = 2
    eat = 0
    answer = 0

    y, x = sy, sx
    while True:
        nxt = find(graph, y, x, shark)
        if nxt != None:
            ny, nx, c = nxt
            graph[ny][nx] = 0
            eat += 1
            if shark == eat:
                shark += 1
                eat = 0
            y, x = ny, nx
            answer += c
            continue
        return answer
    
result = bfs(graph, sy, sx)
print(result)
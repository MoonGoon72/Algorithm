from collections import deque
import sys
input = sys.stdin.readline

INF = int(1e9)
dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]
n = int(input())
graph = []
shark = (0, 0)
for i in range(n):
    line = list(map(int, input().split()))
    for j in range(n):
        if line[j] == 9:
            shark = (i, j)
            line[j] = 0
    graph.append(line)

def check(y, x):
    return 0 <= y < n and 0 <= x < n

def find(graph, size, shark):
    y, x = shark
    visited = [[False] * n for _ in range(n)]
    distance = [[INF] * n for _ in range(n)]
    distance[y][x] = 0
    visited[y][x] = True
    queue = deque([(y, x)])
    candidates = []
    
    while queue:
        y, x = queue.popleft()
        for i in range(4):
            ny, nx = y + dy[i], x + dx[i]
            if not check(ny, nx) or (visited[ny][nx] or graph[ny][nx] > size):
                continue
            distance[ny][nx] = distance[y][x] + 1
            visited[ny][nx] = True
            queue.append((ny, nx))
            if graph[ny][nx] < size and graph[ny][nx] != 0:
                candidates.append((distance[ny][nx], ny, nx))
    
    candidates.sort()
    if candidates:
        return candidates[0]
    return None

def bfs(shark):
    size = 2
    count = 0
    answer = 0
    fish = find(graph, size, shark)
    while fish is not None:
        dist, y, x = fish
        answer += dist
        count += 1
        if count == size:
            size += 1
            count = 0
        graph[y][x] = 0
        shark = (y, x)
        fish = find(graph, size, shark)
    return answer
answer = bfs(shark)
print(answer)
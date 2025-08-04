import sys, itertools, copy
from collections import deque
input = sys.stdin.readline

dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]

n, m = map(int, input().split())
graph = []
empty = []
virus = []
for i in range(n):
    line = list(map(int, input().split()))
    for j in range(m):
        if line[j] == 0:
            empty.append((i, j))
        elif line[j] == 2:
            virus.append((i, j))
    graph.append(line)

def check(y, x):
    return 0 <= y < n and 0 <= x < m

def bfs(arr):
    queue = deque(virus)

    while queue:
        y, x = queue.popleft()
        for i in range(4):
            ny, nx = y + dy[i], x + dx[i]
            if check(ny, nx) and arr[ny][nx] == 0:
                arr[ny][nx] = 2
                queue.append((ny, nx))
    save = 0
    for i in range(n):
        for j in range(m):
            if arr[i][j] == 0:
                save += 1
    return save

combs = itertools.combinations(empty, 3)
answer = 0

for comb in combs:
    copied_graph = copy.deepcopy(graph)
    for y, x in comb:
        copied_graph[y][x] = 1
    answer = max(answer, bfs(copied_graph))
print(answer)
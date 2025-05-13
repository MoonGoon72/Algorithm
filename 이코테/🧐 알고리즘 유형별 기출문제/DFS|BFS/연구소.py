from collections import deque
import sys, copy, itertools
input = sys.stdin.readline

dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]
n, m = map(int, input().split())

def check(y, x):
    return 0 <= y < n and 0 <= x < m

def spread_and_safe_area():
    queue = deque(virus)
    copied_graph = copy.deepcopy(graph)
    while queue:
        y, x = queue.popleft()
        for i in range(4):
            ny, nx = y + dy[i], x + dx[i]
            if check(ny, nx):
                if copied_graph[ny][nx] == 0:
                    copied_graph[ny][nx] = 2
                    queue.append((ny, nx))
    safes = 0
    for i in range(n):
        safes += copied_graph[i].count(0)
    return safes

graph = []
virus = []
empty_space = []

for i in range(n):
    line = list(map(int, input().split()))
    for j in range(m):
        if line[j] == 2:
            virus.append((i, j))
        if line[j] == 0:
            empty_space.append((i, j))
    graph.append(line)
answer = 0

comb = list(itertools.combinations(empty_space, 3)) # 전체 가능 조합
for pos in comb: # pos = 조합 하나 (벽 세개)
    for y, x in pos:
        graph[y][x] = 1
    answer = max(answer, spread_and_safe_area())
    for y, x in pos:
        graph[y][x] = 0
print(answer)
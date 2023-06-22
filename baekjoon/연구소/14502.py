# 백준 14502 연구소 문제
# DFS/BFS 문제
# 1. 벽을 세울 수 있는 모든 경우의 수를 구한다.
# 2. 벽을 세운다.
# 3. 바이러스를 퍼트린다.
# 4. 안전 영역의 크기를 구한다.

from collections import deque
import copy
import sys
input = sys.stdin.readline
from itertools import combinations
n, m = map(int, input().split(' '))

graph = [list(map(int, input().split(' '))) for _ in range(n)]

dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]

result = 0

def check(y, x):
    return 0 <= y < n and 0 <= x < m

def bfs():
    test_graph = copy.deepcopy(graph)

    queue = deque()
    for i in range(n):
        for j in range(m):
            if test_graph[i][j] == 2:
                queue.append((i, j))
    while queue:
        y, x = queue.popleft()
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if check(ny, nx):
                if test_graph[ny][nx] == 0:
                    test_graph[ny][nx] = 2
                    if (ny, nx) not in queue:
                        queue.append((ny, nx))

    count = 0
    global result
    for i in range(n):
        count += test_graph[i].count(0)
    result = max(result, count)

def making_wall(count):
    if count == 3:
        bfs()
        return
    else:
        spaces = []
        for i in range(n):
            for j in range(m):
                if graph[i][j] == 0:
                    graph[i][j] = 1
                    making_wall(count+1)
                    graph[i][j] = 0

making_wall(0)
print(result)
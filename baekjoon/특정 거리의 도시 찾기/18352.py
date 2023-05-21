from collections import deque
import sys
input = sys.stdin.readline
INF = float('infinity')
N, M, K, X = map(int, input().split(' '))

distance = [INF for _ in range(N + 1)]
distance[X] = 0
graph = [[] for _ in range(N + 1)]

for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)

def bfs(start):
    queue = deque([start])
    while queue:
        now = queue.popleft()
        for node in graph[now]:
            if distance[node] > distance[now] + 1:
                distance[node] = distance[now] + 1
                queue.append(node)

bfs(X)
flag = False
for index, num in enumerate(distance):
    if num == K:
        print(index)
        flag = True
if not flag: print(-1)

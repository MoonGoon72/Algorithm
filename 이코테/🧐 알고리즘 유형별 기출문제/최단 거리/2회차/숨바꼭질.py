# https://www.acmicpc.net/problem/6118
from collections import deque
import sys
input = sys.stdin.readline
INF = int(1e9)

n, m = map(int, input().split())
graph = [[] for _ in range(n + 1)]
distance = [INF] * (n + 1)
distance[1] = 0

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

queue = deque([1])

while queue:
    v = queue.popleft()
    for nxt in graph[v]:
        if distance[nxt] > distance[v] + 1:
            distance[nxt] = distance[v] + 1
            queue.append(nxt)

value = max(distance[1:])
index = distance.index(value)
count = distance.count(value)

print(index, value, count)

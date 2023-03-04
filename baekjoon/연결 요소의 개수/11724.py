import sys
input = sys.stdin.readline
from collections import deque
n, m = map(int, input().split(' '))
graph = [[] for _ in range(n + 1)]
visited = [False for _ in range(n + 1)]

for _ in range(m):
    a, b = map(int, input().split(' '))
    graph[a].append(b)
    graph[b].append(a)

def bfs(start):
    if visited[start]: return 0
    queue = deque([start])
    while queue:
        now = queue.popleft()
        visited[now] = True
        for num in graph[now]:
            if not visited[num]:
                queue.append(num)
                visited[num] = True
    return 1

result = 0

for i in range(1, n + 1):
    result += bfs(i)
print(result)
from collections import deque
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
graph = [[] for _ in range(n + 1)]
reverse_graph = [[] for _ in range(n + 1)]

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    reverse_graph[b].append(a)

def bfs(start, graph):
    visited = [False] * (n + 1)
    visited[start] = True
    queue = deque()
    queue.append(start)
    count = 0

    while queue:
        now = queue.popleft()
        for node in graph[now]:
            if not visited[node]:
                queue.append(node)
                visited[node] = True
                count += 1
    return count

result = 0

for i in range(1, n + 1):
    higher = bfs(i, graph)
    lower = bfs(i, reverse_graph)
    if higher + lower == n - 1:
        result += 1

print(result)

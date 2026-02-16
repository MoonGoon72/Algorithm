from collections import deque
import sys
input = sys.stdin.readline

n = int(input())
a, b = map(int, input().split())
m = int(input())
graph = [[] for _ in range(n+1)]

for _ in range(m):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)

def bfs(a, b):
    visited = [False] * (n+1)
    visited[a] = True
    queue = deque()
    queue.append((a, 0))

    while queue:
        now, dist = queue.popleft()
        for nxt in graph[now]:
            if visited[nxt]: continue
            if nxt == b:
                return dist + 1
            queue.append((nxt, dist+1))
            visited[nxt] = True
    return -1

answer = bfs(a, b)
print(answer)
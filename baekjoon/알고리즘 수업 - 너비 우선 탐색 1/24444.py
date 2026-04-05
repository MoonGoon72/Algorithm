from collections import deque
import sys
input = sys.stdin.readline

n, m, r = map(int, input().split())
graph = [[] for _ in range(n + 1)]
visited = [False] * (n + 1)

for _ in range(m):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

for i in range(1, n+1):
    graph[i].sort()

answer = [0] * (n + 1)
queue = deque([r])
visited[r] = True
rank = 1

while queue:
    now = queue.popleft()
    answer[now] = rank
    rank += 1
    
    for nxt in graph[now]:
        if visited[nxt]: continue
        queue.append(nxt)
        visited[nxt] = True
        answer.append(nxt)

for i in range(1, n+1):
    print(answer[i])
from collections import deque
import sys
input = sys.stdin.readline

N, M, V = map(int, input().split())

graph = [[] for _ in range(N+1)]
visited = [False] * (N+1)
for _ in range(M):
    a,b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

def dfs(start):
    stack = [start]
    while stack:
        now = stack.pop()
        if not visited[now]: print(now, end=' ')
        visited[now] = True
        graph[now].sort(reverse=True)  #pop 할때 작은 수부터 나오게 하기 위해
        for i in graph[now]:
            if not visited[i]:
                stack.append(i)

def bfs(start):
    queue = deque([start])
    while queue:
        now = queue.popleft()
        if not visited[now]: print(now, end=' ')
        visited[now] = True
        graph[now].sort()
        for i in graph[now]:
            if not visited[i]:
                queue.append(i)

dfs(V)
print()
visited = [False] * (N + 1)
bfs(V)
print()


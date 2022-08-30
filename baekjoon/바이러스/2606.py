import sys
input = sys.stdin.readline

number = int(input())
pair = int(input())
graph = list([] for _ in range(number + 1))
visited = list(False for _ in range(number + 1))
for _ in range(pair):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

def dfs(start):
    infested = int(-1)
    stack = [start]
    while stack:
        now = stack.pop()
        if not visited[now]:
            infested+=1
            visited[now] = True
            graph[now].sort(reverse=True)
            for i in graph[now]:
                if not visited[i]: stack.append(i)
    print(infested)

dfs(1)
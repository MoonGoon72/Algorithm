from collections import deque, defaultdict
import sys
input = sys.stdin.readline

n, m = map(int, input().split())

graph = [[] for _ in range(m)]
floor_to_elevs = defaultdict(list)
for i in range(m):
    x, y = map(int, input().split())
    for f in range(x, n+1, y):
        floor_to_elevs[f].append(i)

connected = [[False] * m for _ in range(m)]
for elev_list in floor_to_elevs.values():
    for i in range(len(elev_list)):
        for j in range(i+1, len(elev_list)):
            ei, ej = elev_list[i], elev_list[j]
            if not connected[ei][ej]:
                connected[ei][ej] = connected[ej][ei] = True
                graph[ei].append(ej)
                graph[ej].append(ei)

a, b = map(int, input().split())
def bfs(a, b):
    visited = [False for _ in range(m)]
    queue = deque()
    target = set(floor_to_elevs[b])
    for e in floor_to_elevs[a]:
        queue.append((e, 1))
        visited[e] = True

    while queue:
        cur, depth = queue.popleft()
        if cur in target:
            path = []
            node = cur
            while node != -1:
                path.append(node)
                node = parent[node]
            path.reverse()
            return path
        for next_e in graph[cur]:
            if not visited[next_e]:
                visited[next_e] = True
                queue.append((next_e, depth + 1))
                parent[next_e] = cur
    return []

parent = [-1] * m
arr = bfs(a, b)
print(len(arr) if arr else -1)
for e in arr:
    print(e + 1)
        
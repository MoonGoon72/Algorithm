import sys
input = sys.stdin.readline

def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]

def union(a, b):
    a, b = find(a), find(b)
    
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

n, m = map(int, input().split())
parent = [i for i in range(n + 1)]
graph = [[] for _ in range(n + 1)]
routes = []

for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append(b)
    routes.append((c, a, b))
routes.sort()

answer = 0
last = 0
for route in routes:
    c, a, b = route
    if find(a) == find(b):
        continue
    union(a, b)
    answer += c
    last = c
print(answer - last)
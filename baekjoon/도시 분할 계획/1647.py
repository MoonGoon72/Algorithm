import sys, heapq
input = sys.stdin.readline

n, m = map(int, input().split())
parent = [i for i in range(n + 1)]
edge_count = 0
edges = []
q = []

for _ in range(m):
    a, b, c = map(int, input().split())
    heapq.heappush(q, (c, a, b))
    
def find(x):
    if x != parent[x]:
        parent[x] = find(parent[x])
    return parent[x]

def union(x, y):
    px, py = find(x), find(y)
    if px < py:
        parent[py] = px
    elif px > py:
        parent[px] = py
    return

while q:
    dist, x, y = heapq.heappop(q)
    px, py = find(x), find(y)
    if px == py:
        continue
    union(x, y)
    edge_count += 1
    heapq.heappush(edges, - dist)
    if edge_count == n - 1:
        break

heapq.heappop(edges)
answer = - sum(edges)
print(answer)

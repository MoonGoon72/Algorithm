import sys, heapq
input = sys.stdin.readline

n = int(input())
m = int(input())

queue = []

for _ in range(m):
    a, b, c = map(int, input().split())
    heapq.heappush(queue, (c, a, b))

def union(x, y, parent):
    px, py = parent[x], parent[y]
    if px > py:
        parent[px] = py
    else:
        parent[py] = px
    return

def find(x, parent):
    if parent[x] != x:
        parent[x] = find(parent[x], parent)
    return parent[x]

parent = [i for i in range(n + 1)]

cost = 0
connection = 0
while queue or connection < n - 1:
    c, a, b = heapq.heappop(queue)
    if find(a, parent) == find(b, parent):
        continue
    
    union(a, b, parent)
    cost += c
    connection += 1

print(cost)

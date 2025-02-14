import sys, heapq
sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline

v, e = map(int, input().split())
parent = [i for i in range(v + 1)]
q = []
edge_count = 0
answer = 0

for _ in range(e):
    a, b, c = map(int, input().split())
    heapq.heappush(q, (c, a, b))

def find(x):
    px = parent[x]
    if px != x:
        parent[x] = find(parent[x])  # 경로 압축
    return parent[x]

def union(x, y):
    px, py = find(x), find(y)
    if px < py:
        parent[py] = px
    elif px > py:
        parent[px] = py
    return

while q:
    c, a, b = heapq.heappop(q)
    pa, pb = find(a), find(b)
    if pa != pb:
        union(a, b)
        edge_count += 1
        answer += c
        if edge_count == v - 1:
            break

print(answer)
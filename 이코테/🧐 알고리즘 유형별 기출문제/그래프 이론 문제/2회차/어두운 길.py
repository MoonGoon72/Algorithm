import sys
input = sys.stdin.readline

def union(parent, x, y):
    px, py = find(parent, x), find(parent, y)

    if px > py:
        parent[px] = py
    else:
        parent[py] = px 
    return

def find(parent, x):
    if parent[x] != x:
        parent[x] = find(parent, parent[x])
    return parent[x]

while True:
    m, n = map(int, input().split())
    if m == n == 0:
        break

    parent = [i for i in range(m)]
    edges = []
    total = 0
    for _ in range(n):
        x, y, z = map(int, input().split())
        edges.append((z, x, y))
        total += z
    edges.sort()

    answer = 0
    count = 0
    for cost, x, y in edges:
        if count == m - 1:
            break
        px, py = find(parent, x), find(parent, y)
        if px != py:
            union(parent, x, y)
            answer += cost
            count += 1

    print(total - answer)
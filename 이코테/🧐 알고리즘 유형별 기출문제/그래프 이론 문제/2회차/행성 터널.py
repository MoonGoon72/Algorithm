import sys
input = sys.stdin.readline

n = int(input())
parent = [i for i in range(n)]
x = []
y = []
z = []

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

for i in range(n):
    a, b, c = map(int, input().split())
    x.append((a, i))
    y.append((b, i))
    z.append((c, i))

x.sort()
y.sort()
z.sort()

edges = []

for i in range(n - 1):
    edges.append((abs(x[i][0] - x[i + 1][0]), x[i][1], x[i + 1][1]))
    edges.append((abs(y[i][0] - y[i + 1][0]), y[i][1], y[i + 1][1]))
    edges.append((abs(z[i][0] - z[i + 1][0]), z[i][1], z[i + 1][1]))

edges.sort()

answer = 0
count = 0
for cost, a, b in edges:
    if count == n - 1:
        break

    if find(parent, a) == find(parent, b):
        continue

    union(parent, a, b)
    answer += cost
    count += 1

print(answer)
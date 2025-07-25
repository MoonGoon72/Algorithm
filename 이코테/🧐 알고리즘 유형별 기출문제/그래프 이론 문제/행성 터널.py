import sys
input = sys.stdin.readline

def find(x):
    if parents[x] != x:
        parents[x] = find(parents[x])
    return parents[x]

def union(x, y):
    px, py = find(x), find(y)
    
    if px < py:
        parents[py] = px
    else:
        parents[px] = py
    return

n = int(input())
parents = [i for i in range(n)]
edges = []

x = []
y = []
z = []

for i in range(n):
    data = list(map(int, input().split()))
    x.append((data[0], i))
    y.append((data[1], i))
    z.append((data[2], i))

x.sort()
y.sort()
z.sort()

for i in range(n - 1):
    edges.append((x[i + 1][0] - x[i][0], x[i + 1][1], x[i][1]))
    edges.append((y[i + 1][0] - y[i][0], y[i + 1][1], y[i][1]))
    edges.append((z[i + 1][0] - z[i][0], z[i + 1][1], z[i][1]))
edges.sort()

answer = 0
for edge in edges:
    weight, a, b = edge
    pa, pb = find(a), find(b)
    if pa != pb:
        union(a, b)
        answer += weight
print(answer)
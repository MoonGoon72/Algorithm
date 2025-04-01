import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

def direction_pos(s):
    if s == "U":
        return (-1, 0)
    elif s == "D":
        return (1, 0)
    elif s == "L":
        return (0, -1)
    else:
        return (0, 1)

def find(y, x):
    if parent[y][x] != (y, x):
        parent[y][x] = find(*parent[y][x])
    return parent[y][x]

def union(y1, x1, y2, x2):
    root1 = find(y1, x1)
    root2 = find(y2, x2)
    if root1 != root2:
        parent[root2[0]][root2[1]] = root1
    return

n, m = map(int, input().split())

graph = []
for _ in range(n):
    graph.append(input())

parent = [[(i, j) for j in range(m)]for i in range(n)]

for y in range(n):
    for x in range(m):
        dy, dx = direction_pos(graph[y][x])
        ny, nx = y + dy, x + dx
        union(y, x, ny, nx)

unique = set(find(y, x) for y in range(n) for x in range(m))
print(len(unique))

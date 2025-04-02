import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

n, m = map(int, input().split())
graph = [input().strip() for _ in range(n)]
parent = [[(r, c) for c in range(m)] for r in range(n)]

def next_direction(s):
    if s == "D":
        return (1, 0)
    elif s == "L":
        return (0, -1)
    elif s == "R":
        return (0, 1)
    else:
        return (-1, 0)

def find(r, c):
    if parent[r][c] != (r, c):
        parent[r][c] = find(*parent[r][c])
    return parent[r][c]

def union(from_pos, to_pos):
    root1 = find(*from_pos)
    root2 = find(*to_pos)
    if root1 != root2:
        parent[root2[0]][root2[1]] = root1
    return

for r in range(n):
    for c in range(m):
        dy, dx = next_direction(graph[r][c])
        ny, nx = r + dy, c + dx
        union((r, c), (ny, nx))

unique_set = { find(i, j) for j in range(m) for i in range(n)}
answer = len(unique_set)
print(answer)

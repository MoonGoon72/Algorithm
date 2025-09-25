import sys
input = sys.stdin.readline

def union(x, y):
    px, py = find(x), find(y)

    if px > py:
        parent[px] = py
    else:
        parent[py] = px
    return

def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]

n = int(input())
m = int(input())

parent = [i for i in range(n + 1)]

for i in range(1, n + 1):
    data = list(map(int, input().split()))
    for j in range(n):
        if data[j] == 1:
            if find(i) != find(j + 1):
                union(i, j + 1)

plan = list(map(int, input().split()))
px = find(plan[0])
is_possible = True

for c in plan:
    if find(c) != px:
        is_possible = False
        break

print("YES" if is_possible else "NO")
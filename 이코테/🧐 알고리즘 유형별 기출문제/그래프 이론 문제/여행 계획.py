# 백준 1976 여행 가자

import sys
input = sys.stdin.readline

n = int(input())
m = int(input())

graph = [[] for _ in range(n + 1)]
parent = [i for i in range(n + 1)]

def union(x, y):
    px, py = find(x), find(y)
    
    if px < py:
        parent[py] = px
    elif px > py:
        parent[px] = py
    return

def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]

for i in range(1, n + 1):
    connections = [0] + list(map(int, input().split()))
    for j in range(1, n + 1):
        if connections[j]:
            pi, pj = find(i), find(j)
            if pi != pj:
                union(i, j)

plan = list(map(int, input().split()))

for i in range(1, n + 1):
    find(i)

result = find(plan[0])
for p in plan:
    if result != find(p):
        print("NO")
        exit(0)
print("YES")
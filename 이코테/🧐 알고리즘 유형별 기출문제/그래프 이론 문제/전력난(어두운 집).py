# boj.kr/6497
import sys
input = sys.stdin.readline

def union(x, y):
    px, py = find(x), find(y)

    if px == py: 
        return

    if px < py:
        parents[py] = px
    else:
        parents[px] = py
    return

def find(x):
    if parents[x] != x:
        parents[x] = find(parents[x])
    return parents[x]

def minimum_spanning_tree():
    answer = 0
    for edge in edges:
        weight, x, y = edge
        px, py = find(x), find(y)
        
        if px != py:
            answer += weight
            union(px, py)
    return answer

while True:
    m, n = map(int, input().split())
    if m == 0 and n == 0: 
        break
    
    parents = [i for i in range(m)]
    edges = []
    sum_of_weight = 0
    for _ in range(n):
        x, y, z = map(int, input().split())
        edges.append((z, x, y))
        sum_of_weight += z
    edges.sort()
    mst_weight = minimum_spanning_tree()
    print(sum_of_weight - mst_weight)
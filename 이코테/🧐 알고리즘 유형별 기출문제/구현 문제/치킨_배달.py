from collections import deque
import sys, itertools
input = sys.stdin.readline
INF = 1e9

def calc(chicken):
    h = len(house)
    dist = [INF] * h
    for cy, cx in chicken:
        for i in range(h):
            hy, hx = house[i]
            dist[i] = min(dist[i], abs(cy - hy) + abs(cx - hx))
    return sum(dist)

n, m = map(int, input().split())
graph = []
chicken, house = [], []

for i in range(n):
    rows = list(map(int, input().split()))
    graph.append(rows)
    
    for j in range(n):
        if rows[j] == 2:
            chicken.append((i, j))
        elif rows[j] == 1:
            house.append((i, j))

chicken_comb = list(itertools.combinations(chicken, m))
answer = INF

for chicken in chicken_comb:
    answer = min(calc(chicken), answer)

print(answer)
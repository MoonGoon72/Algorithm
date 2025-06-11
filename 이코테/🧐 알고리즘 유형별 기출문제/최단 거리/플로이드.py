# boj 11404

import sys
input = sys.stdin.readline

inf = int(1e9)
n = int(input())
m = int(input())
distance = [[inf] * (n + 1) for _ in range(n + 1)]

for _ in range(m):
    a, b, c = map(int, input().split())
    distance[a][b] = min(distance[a][b], c)

for i in range(1, n + 1):
    distance[i][i] = 0

for k in range(1, n + 1):
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            if distance[i][j] > distance[i][k] + distance[k][j]:
                distance[i][j] = distance[i][k] + distance[k][j]

for i in range(1, n + 1):
    for j in range(1, n + 1):
        print(distance[i][j] if distance[i][j] != inf else 0, end=" ")
    print()
import sys
input = sys.stdin.readline
inf = int(1e9)

n = int(input())
m = int(input())

graph = [[inf] * (n + 1) for _ in range(n + 1)]

for _ in range(m):
    a, b, c = map(int, input().split())
    if graph[a][b] > c:
        graph[a][b] = c

for i in range(1, n + 1):
    graph[i][i] = 0

for k in range(1, n + 1):
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            graph[i][j] = min(graph[i][k] + graph[k][j], graph[i][j])

for i in range(1, n + 1):
    for j in range(1, n + 1):
        print(0 if graph[i][j] == inf else graph[i][j], end=" ")
    print()
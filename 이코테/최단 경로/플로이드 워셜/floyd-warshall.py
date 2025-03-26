import sys
input = sys.stdin.readline
INF = int(1e9)

def floyd_washall():
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            for k in range(1, n + 1):
                graph[j][k] = min(graph[j][k], graph[j][i] + graph[i][k])
    return

n = int(input())
m = int(input())
graph = [[INF] * (n + 1) for _ in range(n + 1)]

for _ in range(m):
    a, b, d = map(int, input().split())
    graph[a][b] = d

for i in range(n + 1):
    graph[i][i] = 0

floyd_washall()

for a in range(1, n + 1):
    for b in range(1, n + 1):
        if graph[a][b] == INF:
            print("INFINITY", end=" ")
        else:
            print(graph[a][b], end=" ")
    print()
"""
input
4
7
1 2 4
1 4 6
2 1 3
2 3 7
3 1 5
3 4 4
4 3 2
"""
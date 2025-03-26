import sys
input = sys.stdin.readline
INF = int(1e9)

def floyd_warshall():
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            for k in range(1, n + 1):
                graph[j][k] = min(graph[j][k], graph[j][i] + graph[i][k])

n, m = map(int, input().split())
graph = [[INF] * (n + 1) for _ in range(n + 1)]
for _ in range(m):
    a, b = map(int, input().split())
    graph[a][b] = 1
    graph[b][a] = 1
for i in range(1, n + 1):
    graph[i][i] = 0

x, k = map(int, input().split())
floyd_warshall()
answer = graph[1][k] + graph[k][x]
print(answer if answer < INF else -1)

"""
5 7
1 2
1 3
1 4
2 4
3 4
3 5
4 5
4 5

answer: 3
"""
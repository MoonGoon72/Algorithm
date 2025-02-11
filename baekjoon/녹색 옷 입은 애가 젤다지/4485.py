from collections import deque
import sys, heapq
input = sys.stdin.readline

def movalbe(y, x, n):
    return 0 <= y < n and 0 <= x < n

dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]
answer = []

while True:
    n = int(input())
    if n == 0: 
        break
    graph = list(list(map(int, input().split())) for _ in range(n))
    distance = [[int(1e9)] * n for _ in range(n)]
    q = []
    heapq.heappush(q, (graph[0][0], 0 ,0)) # y, x, cost
    distance[0][0] = graph[0][0]

    while q:
        dist, y, x = heapq.heappop(q)
        if distance[y][x] < dist:
            continue
        for i in range(4):
            ny, nx = y + dy[i], x + dx[i]
            if movalbe(ny, nx, n):
                cost = dist + graph[ny][nx]
                if cost < distance[ny][nx]:
                    distance[ny][nx] = cost
                    heapq.heappush(q, (distance[ny][nx], ny, nx))
    answer.append(distance[n - 1][n - 1])

for i, e in enumerate(answer):
    print(f"Problem {i + 1}: {e}")
# https://www.acmicpc.net/problem/4485

import sys, heapq
input = sys.stdin.readline

INF = int(1e9)
dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]

def check(y, x, n):
    return 0 <= y < n and 0 <= x < n

answers = []
count = 1

while True:
    n = int(input())
    if n == 0: break

    graph = list(list(map(int, input().split())) for _ in range(n))
    distance = [[INF] * n for _ in range(n)]
    distance[0][0] = graph[0][0]
    queue = [(distance[0][0], 0, 0)]
    while queue:
        c, y, x = heapq.heappop(queue)
        if c > distance[y][x]:
            continue
        for i in range(4):
            ny, nx = y + dy[i], x + dx[i]
            if check(ny, nx, n):
                if distance[ny][nx] > distance[y][x] + graph[ny][nx]:
                    distance[ny][nx] = distance[y][x] + graph[ny][nx]
                    heapq.heappush(queue, (distance[ny][nx], ny, nx))
    answers.append((count, distance[n-1][n-1]))
    count += 1

for answer in answers:
    print(f'Problem {answer[0]}: {answer[1]}')
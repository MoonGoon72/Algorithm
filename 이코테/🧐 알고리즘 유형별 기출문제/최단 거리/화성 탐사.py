import heapq
import sys
input = sys.stdin.readline

inf = int(1e9)
t = int(input())

dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]

def check(y, x, n):
    return 0 <= y < n and 0 <= x < n

def dijkstra(board, n):
    distance = [[inf] * n for _ in range(n)]
    distance[0][0] = board[0][0]
    queue = [(distance[0][0], 0, 0)]
    
    while queue:
        c, y, x = heapq.heappop(queue)
        
        if distance[y][x] < c: # 이미 이전에 갱신되었기 때문에 반영할 필요가 없음
            continue

        for i in range(4):
            ny, nx = y + dy[i], x + dx[i]
            if check(ny, nx, n):
                next_cost = board[ny][nx] + c
                if distance[ny][nx] > next_cost:
                    distance[ny][nx] = next_cost
                    heapq.heappush(queue, (next_cost, ny, nx))
    return distance[n - 1][n - 1]

for _ in range(t):
    n = int(input())
    board = list(list(map(int, input().split())) for _ in range(n))
    answer = dijkstra(board, n)
    print(answer)

"""
3
3
5 5 4
3 9 1
3 2 7
5
3 7 2 0 1
2 8 0 9 1
1 2 1 8 1
9 8 9 2 0
3 6 5 1 5
7
9 0 5 1 1 5 3
4 1 2 1 6 5 3
0 7 6 1 6 8 5
1 1 7 8 3 2 3
9 4 0 7 6 4 1
5 8 3 2 4 8 3
7 4 8 4 8 3 4

--- 출력 ---
20
19
36
"""

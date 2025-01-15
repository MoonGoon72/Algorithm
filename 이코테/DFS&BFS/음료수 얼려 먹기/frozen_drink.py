from collections import deque
import sys
input = sys.stdin.readline

r, c = map(int, input().split())
graph = list(list(map(int, input().strip())) for _ in range(r))
visited = [[False] * c for _ in range(r)]

dy = [-1 ,1, 0, 0]
dx = [0, 0, -1, 1]

def check(y, x):
    return 0 <= y < r and 0 <= x < c

def bfs(y, x):
    queue = deque()
    queue.append((y, x))
    visited[y][x] = True

    while queue:
        y, x = queue.popleft()
        for i in range(4):
            ny, nx = y + dy[i], x + dx[i]
            if check(ny, nx):
                if not visited[ny][nx] and graph[ny][nx] == 0:
                    queue.append((ny, nx))
                    visited[ny][nx] = True
    return

def solution():
    answer = 0
    for row in range(r):
        for col in range(c):
            if not visited[row][col] and graph[row][col] != 1:
                bfs(row, col)
                answer += 1
    print(answer)

solution()
"""
4 5
00110
00011
11111
00000

15 14
00000111100000
11111101111110
11011101101110
11011101100000
11011111111111
11011111111100
11000000011111
01111111111111
00000000011111
01111111111000
00011111111000
00000011111000
11111111110011
11100011111111
11100011111111
"""
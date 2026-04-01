from collections import deque
import sys
input = sys.stdin.readline

dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]

n, m = map(int, input().split())
board = [list(map(str, input().rstrip())) for _ in range(m)]
visited = [[False for _ in range(n)] for _ in range(m)]

def check(y, x):
    return 0 <= y < m and 0 <= x < n

def bfs(r, c):
    count = 1
    value = board[r][c]
    queue = deque([(r, c)])
    visited[r][c] = True
    while queue:
        y, x = queue.popleft()
        for i in range(4):
            ny, nx = y + dy[i], x + dx[i]
            if not check(ny, nx): continue
            if visited[ny][nx] or board[ny][nx] != value: continue
            queue.append((ny, nx))
            visited[ny][nx] = True
            count += 1
    return count ** 2

result = [0, 0]
for r in range(m):
    for c in range(n):
        if not visited[r][c]:
            value = board[r][c]
            cost = bfs(r, c)
            result[0 if value == "W" else 1] += cost
print(*result)
from collections import deque
import sys
input = sys.stdin.readline

dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]

n, l, r = map(int, input().split())
board = list(list(map(int, input().split())) for _ in range(n))

def check(y, x):
    return 0 <= y < n and 0 <= x < n

def bfs(row, col, visited):
    queue = deque()
    queue.append((row, col))
    visited[row][col] = True
    federation = [(row, col)]
    
    while queue:
        y, x = queue.popleft()

        for i in range(4):
            ny, nx = y + dy[i], x + dx[i]
            if not check(ny, nx) or visited[ny][nx]:
                continue
            if l <= abs(board[y][x] - board[ny][nx]) <= r:
                federation.append((ny, nx))
                queue.append((ny, nx))
                visited[ny][nx] = True
    if len(federation) == 1:
        return False
    average = sum(board[row][col] for row, col in federation) // len(federation)
    for row, col in federation:
        board[row][col] = average
    return True

count = 0
while True:
    visited = list([False] * n for _ in range(n))
    moved = False
    for row in range(n):
        for col in range(n):
            if not visited[row][col]:
                if bfs(row, col, visited):
                    moved = True

    if not moved:
        break
    else:
        count += 1

print(count)
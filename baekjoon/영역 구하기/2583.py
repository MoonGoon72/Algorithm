import sys
input = sys.stdin.readline

dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]

m, n, k = map(int, input().split())
board = [[0] * n for _ in range(m)]

for _ in range(k):
    x1, y1, x2, y2 = map(int, input().split()) # 왼쪽 아래, 오른 쪽 위
    for row in range(y1, y2):
        for col in range(x1, x2):
            board[row][col] = 1
    
def check(x, y):
    return 0 <= x < n and 0 <= y < m

def dfs(r, c, board):
    count = 1
    stack = [(r, c)]
    board[r][c] = 1
    while stack:
        y, x = stack.pop()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if check(nx, ny) and not board[ny][nx]:
                board[ny][nx] = 1
                count += 1
                stack.append((ny, nx))
    
    return count

sections = []
for row in range(m):
    for col in range(n):
        if not board[row][col]:
            sections.append(dfs(row, col, board))

sections.sort()
print(len(sections))
print(*sections)
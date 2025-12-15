from collections import deque, defaultdict
import sys
input = sys.stdin.readline

dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]

n, m = map(int, input().split())
board = []

iceburg_cells = []
for i in range(n):
    line = list(map(int, input().split()))
    for j in range(m):
        if line[j] != 0:
            iceburg_cells.append((i, j))
    board.append(line)

def check(y, x):
    return 0 <= y < n and 0 <= x < m

# 빙산이 녹는 것을 확인하려면 빙산 주위에 바닷물이 얼마나 많은 지를 확인해야 함.

def bfs(r, c, visited):
    seas = defaultdict(int)
    visited[r][c] = True
    queue = deque()
    queue.append((r, c))

    while queue:
        y, x = queue.popleft()
        for d in range(4):
            ny, nx = y + dy[d], x + dx[d]
            if not check(ny, nx): continue

            if board[ny][nx] == 0:
                seas[(y, x)] += 1
                continue
            if not visited[ny][nx]:
                queue.append((ny, nx))
                visited[ny][nx] = True
    for sea in seas:
        y, x = sea
        board[y][x] = max(0, board[y][x] - seas[sea])
        
        if board[y][x] == 0:
            iceburg_cells.remove((y, x))
    return

time = 0
while True:
    visited = [[False] * m for _ in range(n)]
    if not iceburg_cells:
        print(0)
        break
    
    r, c = iceburg_cells[0]
    visited[r][c] = True
    bfs(r, c, visited)

    for iceburg in iceburg_cells:
        if not visited[iceburg[0]][iceburg[1]]:
            print(time)
            exit(0)

    time += 1
import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

n, m = map(int, input().split())
graph = []
for _ in range(n):
    line = list(map(int, input().split()))
    graph.append(line)

dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]
visited = [[False] * m for _ in range(n)]

def make_t(y, x):
    return [[(y, x), (y, x + 1), (y, x + 2), (y + 1, x + 1)],
            [(y, x), (y, x - 1), (y, x - 2), (y + 1, x - 1)],
            [(y, x), (y, x + 1), (y, x + 2), (y - 1, x + 1)],
            [(y, x), (y - 1, x), (y - 2, x), (y - 1, x + 1)],
            [(y, x), (y, x - 1), (y, x - 2), (y - 1, x - 1)],
            [(y, x), (y + 1, x), (y + 2, x), (y + 1, x - 1)]]

def check(y, x):
    return 0 <= y < n and 0 <= x < m

def check_t(tetromino):
    for y, x in tetromino:
        if not (0 <= y < n and 0 <= x < m):
            return False
    return True

def calc_t(tetromino):
    cnt = 0
    for y, x in tetromino:
        cnt += graph[y][x]
    return cnt
answer = 0

def dfs(graph, depth, count, y, x):
    global answer
    if depth == 4:
        answer = max(answer, count)
        return
    
    for i in range(4):
        ny, nx = y + dy[i], x + dx[i]
        if not check(ny, nx) or visited[ny][nx]:
            continue
        
        visited[ny][nx] = True
        dfs(graph, depth + 1, count + graph[ny][nx], ny, nx)
        visited[ny][nx] = False

for i in range(n):
    for j in range(m):
        visited[i][j] = True
        dfs(graph, 1, graph[i][j], i, j)
        visited[i][j] = False
        t_blocks = make_t(i, j)
        for t_block in t_blocks:
            if check_t(t_block):
                answer = max(answer, calc_t(t_block))

print(answer)

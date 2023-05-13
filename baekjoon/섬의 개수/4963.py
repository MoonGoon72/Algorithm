import sys
input = sys.stdin.readline
dy = [-1, 1, 0, 0, 1, -1, 1, -1]
dx = [0, 0, -1, 1, -1, 1, 1, -1]

def dfs(y, x):
    tmp_result = 0
    stack = [(y, x)]
    while stack:
        now_y, now_x = stack.pop()
        if graph[now_y][now_x] == 1:
            graph[now_y][now_x] = 0
            tmp_result = 1
            for i in range(8):
                ny = now_y + dy[i]
                nx = now_x + dx[i]
                if 0 <= ny < h and 0 <= nx < w and graph[ny][nx] == 1:
                    stack.append((ny, nx))
    return tmp_result

while True:
    result = 0
    w, h = map(int, input().split(' '))
    if h == 0 and w == 0: exit()
    graph = [list(map(int, input().split(' '))) for _ in range(h)]

    for row in range(h):
        for col in range(w):
            result += dfs(row, col)
    print(result)

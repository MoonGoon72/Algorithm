from copy import deepcopy
import sys
input = sys.stdin.readline

dx = [-1, -1, 0, 1, 1, 1, 0, -1]
dy = [0, -1, -1, -1, 0, 1, 1, 1]

graph = [[(0, 0) for _ in range(4)] for _ in range(4)]
fishes = dict()

for i in range(1, 17):
    fishes[i] = None

for i in range(4):
    line = list(map(int, input().split()))
    for j in range(4):
        fish, direction = line[j * 2], line[j * 2 + 1]
        graph[i][j] = (fish, direction - 1)
        fishes[fish] = (i, j)

def check(x, y):
    return 0 <= x < 4 and 0 <= y < 4

def swap_fish(x1, y1, x2, y2, fishes, graph):
    if graph[x2][y2] is None:
        (a, ad) = graph[x1][y1]
        fishes[a] = (x2, y2)
        graph[x2][y2] = (a, ad)
        graph[x1][y1] = None
    else:
        (a, ad) = graph[x1][y1]
        (b, bd) = graph[x2][y2]
        graph[x1][y1] = (b, bd)
        graph[x2][y2] = (a, ad)
        fishes[b] = (x1, y1)
        fishes[a] = (x2, y2)

def fish_move(fishes, graph, shark_x, shark_y):
    for i in range(1, 17):
        value = fishes[i]
        if value is None:
            continue
        (x, y) = value
        d = graph[x][y][1]

        for _ in range(8):
            nx, ny = x + dx[d], y + dy[d]
            if check(nx, ny) and (nx != shark_x or ny != shark_y):
                swap_fish(x, y, nx, ny, fishes, graph)
                break
            else:
                d = (d + 1) % 8
                graph[x][y] = (i, d)

def solution(graph, fishes, x, y, d, score):
    global result
    fish_move(fishes, graph, x, y)
    result = max(result, score)
    nx, ny = x, y
    
    while True:
        # 상어 움직임
        nx, ny = nx + dx[d], ny + dy[d]

        if check(nx, ny):
            if graph[nx][ny] is not None:
                # 물고기 냠
                (fish, fd) = graph[nx][ny]
                new_graph = deepcopy(graph)
                new_fishes = deepcopy(fishes)
                new_graph[nx][ny] = None
                new_fishes[fish] = None
                solution(new_graph, new_fishes, nx, ny, fd, score + fish)
        else:
            break
    return
    
result = 0
fish, d = graph[0][0]
graph[0][0] = None
fishes[fish] = None
solution(graph, fishes, 0, 0, d, fish)

print(result)
from copy import deepcopy
import sys
input = sys.stdin.readline

dy = [-1, -1, 0, 1, 1, 1, 0, -1]
dx = [0, -1, -1, -1, 0, 1, 1, 1]

graph = []
fish = [(-1, -1)] * 17
direction = [0] * 17
shark = (0, 0)
sd = 0
for i in range(4):
    line = list(map(int, input().split()))
    fishes = []
    for j in range(4):
        fish_num, d = line[j * 2], line[j * 2 + 1] - 1
        fishes.append(fish_num)
        fish[fish_num] = (i, j)
        direction[fish_num] = d
    graph.append(fishes)

def check(y, x):
    return 0 <= y < 4 and 0 <= x < 4

def fish_move(fish, direction, graph):
    for f in range(1, 17):
        if fish[f] == (-1, -1):
            continue
        y, x = fish[f]
        d = direction[f]
        for i in range(8):
            nd = (d + i) % 8
            ny, nx = y + dy[nd], x + dx[nd]
            if not check(ny, nx) or graph[ny][nx] == 17:
                continue
            direction[f] = nd
            if graph[ny][nx] == 0:
                fish[f] = (ny, nx)
                graph[ny][nx] = f
                graph[y][x] = 0
            else:
                nf = graph[ny][nx]
                graph[y][x] = nf
                graph[ny][nx] = f
                fish[f] = (ny, nx)
                fish[nf] = (y, x)
            break

def next_position(graph, shark, sd):
    y, x = shark
    candidates = []
    for _ in range(4):
        y, x = y + dy[sd], x + dx[sd]
        if not check(y, x):
            break
        if graph[y][x] != 0:
            candidates.append((y, x))
    return candidates

answer = 0
def backtracking(graph, fish, direction, shark, sd, count):
    fish_move(fish, direction, graph)
    global answer
    answer = max(answer, count)
    candidates = next_position(graph, shark, sd)

    for ny, nx in candidates:
        c_graph = deepcopy(graph)
        c_direction = deepcopy(direction)
        c_fish = deepcopy(fish)

        nf = graph[ny][nx]
        nsd = c_direction[nf]

        sy, sx = shark
        c_graph[sy][sx] = 0
        c_graph[ny][nx] = 17
        c_fish[nf] = (-1, -1)
        
        backtracking(c_graph, c_fish, c_direction, (ny, nx), nsd, count + nf)

f = graph[0][0]
graph[0][0] = 17
fish[f] = (-1, -1)
sd = direction[f]
shark = (0, 0)
backtracking(graph, fish, direction, shark, sd, f)
print(answer)
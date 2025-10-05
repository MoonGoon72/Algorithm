from copy import deepcopy
from collections import deque
import sys
input = sys.stdin.readline
#     ↑,  ↖, ←,  ↙, ↓, ↘, →, ↗
dx = [-1, -1, 0, 1, 1, 1, 0, -1]
dy = [0, -1, -1, -1, 0, 1, 1, 1]

graph = [[] for _ in range(4)]
fishes = [(-1, -1, -1) for _ in range(17)]  # x, y, d

for i in range(4):
    line = list(map(int, input().split()))
    for j in range(4):
        num, direction = line[j * 2], line[j * 2 + 1]
        graph[i].append(num)
        fishes[num] = (i, j, direction - 1)

def check(x, y):
    return 0 <= x < 4 and 0 <= y < 4

def fish_move(graph, fishes):
    for fish in range(1, 17):
        if fishes[fish] == (-1, -1, -1):
            continue
        x, y, d = fishes[fish]
        for i in range(8):
            nd = (d + i) % 8
            nx, ny = x + dx[nd], y + dy[nd]
            if not check(nx, ny) or graph[nx][ny] == 17:
                continue
            if graph[nx][ny] == 0:  # 비어 있는 경우
                graph[x][y] = 0
                graph[nx][ny] = fish
                fishes[fish] = (nx, ny, nd)
            else:  # 두 개 위치 바꾸기
                other = graph[nx][ny]
                ox, oy, od = fishes[other]
                graph[x][y] = other
                graph[ox][oy] = fish
                fishes[fish] = (ox, oy, nd)
                fishes[other] = (x, y, od)
            break
    return

def eattable_fish(graph, shark):
    x, y, d = shark
    fishes = []
    while True:
        x, y = x + dx[d], y + dy[d]
        if check(x, y):
            if graph[x][y] != 0:
                fishes.append(graph[x][y])
        else:
            break
    return fishes

def backtracking(shark, graph, fishes, count):
    global result
    result = max(result, count)
    fish_move(graph, fishes)
    eattable_fishes = eattable_fish(graph, shark)
    x, y, d = shark
    for fish in eattable_fishes:
        nx, ny, nd = fishes[fish]
        graph_copy = deepcopy(graph)
        fishes_copy = deepcopy(fishes)
        graph_copy[x][y] = 0
        graph_copy[nx][ny] = 17
        fishes_copy[fish] = (-1, -1, -1)
        backtracking((nx, ny, nd), graph_copy, fishes_copy, count + fish)
    return

result = 0
fish = graph[0][0]
shark = (0, 0, fishes[fish][2]) # x, y, d
count = fish
fishes[fish] = (-1, -1, -1)
graph[0][0] = 17

backtracking(shark, graph, fishes, count)
print(result)
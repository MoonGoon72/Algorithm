import itertools, sys
input = sys.stdin.readline

dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]

n = int(input())
data = []
teachers = []
students = []
empty = []

for i in range(n):
    line = list(map(str, input().split()))
    for j in range(n):
        if line[j] == "S":
            students.append((i, j))
        elif line[j] == "T":
            teachers.append((i, j))
        else:
            empty.append((i, j))
    data.append(line)

def check(y, x):
    return 0 <= y < n and 0 <= x < n

def dfs(graph, y, x):
    for i in range(4):
        ny, nx = y, x
        ny, nx = ny + dy[i], nx + dx[i]
        while check(ny, nx) and (graph[ny][nx] != 'T' and graph[ny][nx] != 'O'):
            if graph[ny][nx] == 'S':
                return False
            ny, nx = ny + dy[i], nx + dx[i]
    return True

wallComb = itertools.combinations(empty, 3)
flag = True
for walls in wallComb:
    flag = True
    for y, x in walls:
        data[y][x] = 'O'

    for teacher in teachers:
        flag = dfs(data, teacher[0], teacher[1])
        if not flag:
            break
    if flag:
        break

    for y, x in walls:
        data[y][x] = 'X'

print('YES' if flag else 'NO')
import sys
input = sys.stdin.readline

NORTH = 0
EAST = 1
SOUTH = 2
WEST = 3
# 0 -> 3, 1 -> 0, 2 -> 1, 3 -> 2
dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]

n, m = map(int, input().split())
a, b, direction = map(int, input().split())
graph = list(list(map(int, input().split())) for _ in range(n))
visited = [[False] * m for _ in range(n)]
visited[a][b] = True                                 

def check(y, x):
    return 0 <= y < n and 0 <= x < m

def turn_left():
    global direction
    direction -= 1
    if direction == -1:
        direction = 3
    return

count = 1
turn_time = 0

while True:
    turn_left()
    turn_time += 1
    # 탈출조건
    if turn_time == 4:
        a -= dy[direction]
        b -= dx[direction]
        if graph[a][b] == 1:
            break
        else:
            turn_time = 0
            continue
    
    na = a + dy[direction]
    nb = b + dx[direction]

    if check(na, nb) and graph[na][nb] == 0:
        if not visited[na][nb]:
            visited[na][nb] = True
            count += 1
            a, b = na, nb
            turn_time = 0

print(count)

"""
4 4
1 1 0
1 1 1 1
1 0 0 1
1 1 0 1
1 1 1 1
"""
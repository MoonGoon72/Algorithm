import sys
from collections import deque
input = sys.stdin.readline

row, col = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(col)]
days = int(0)
queue = deque([])
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# 처음에 토마토가 있는 좌표를 저장
for i in range(col):
    for j in range(row):
        if(graph[i][j] == 1): queue.append([i,j])


def bfs():

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if (nx >= 0 and ny >= 0 and nx < col and ny < row and graph[nx][ny] == 0):
                #다음 좌표에 1씩 더해주면 하루씩 증가하는것과 마찬가지이고, popleft를 사용하기때문에 익은 토마토의 위치가 다르더라도 필요 이상으로 익는 경우가 발생하지 않는다.
                graph[nx][ny] = graph[x][y] + 1
                queue.append([nx,ny])

bfs()
for i in graph:
    for j in i:
        if j == 0:
            print("-1")
            exit(0)
    days = max(days, max(i))
print(days -1)
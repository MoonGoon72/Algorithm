import sys
input = sys.stdin.readline

testCase = int(input())
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
def dfs():
    worm = int(0)
    stack = []
    for i in range(col):
        for j in range(row):
            if graph[i][j] != 0:
                stack.append((i,j))
                worm+=1
                graph[i][j] = 0

                while stack:
                    a, b = stack.pop()
                    for k in range(4):
                        nx = a + dx[k]  #상하 (문제 상 y)
                        ny = b + dy[k]  #좌우 (문제 상 x)
                        if(nx >= 0 and ny >= 0 and nx<col and ny < row and graph[nx][ny] == 1):
                            stack.append((nx,ny))
                            graph[nx][ny] = 0
    print(worm)
    
for _ in range(testCase):
    row, col, num = map(int, input().split()) #row == 가로 길이 col == 세로 길이
    graph = [[0 for _ in range(row)] for _ in range(col)]
    for _ in range(num):
        x, y = map(int, input().split())  # x == 가로 좌표 y == 세로 좌표
        graph[y][x] = 1
    dfs()


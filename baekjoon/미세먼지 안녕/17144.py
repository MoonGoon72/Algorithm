import sys
input = sys.stdin.readline

dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]

r, c, t = map(int, input().split())
graph = list(list(map(int, input().split())) for _ in range(r))
answer = 2
def check(y, x):
    return 0 <= y < r and 0 <= x < c and graph[y][x] != -1

def findAirCirculator():
    for y in range(r):
        if graph[y][0] == -1:
            return (y, y+1)

def diffusion():
    # 확산은 전방향 동시에 이루어진다. -> 각자 확산 하고 마무리로 합을 구한다.
    global graph
    tmp = [[0] * c for _ in range(r)]
    for y in range(r):
        for x in range(c):
            if graph[y][x] != 0 and graph[y][x] != -1:
                for i in range(4):
                    ny, nx = y + dy[i], x + dx[i]
                    if check(ny, nx):
                        dust = graph[y][x] // 5
                        if dust > 0:
                            tmp[ny][nx] += dust
                            tmp[y][x] -= dust
    # 시간복잡도 곱창나는데 이러면;
    for y in range(r):
        for x in range(c):
            graph[y][x] += tmp[y][x]
    return

def operateAirCirculator(up, down):
    # 바람 부는 방향 반대서부터 착착착 넣어준다.
    # col = 0 -> row = 0 -> col = c - 1 -> row = 공청기 
    global graph
    # 0. 공청기 위아래
    graph[up - 1][0] = 0
    graph[down + 1][0] = 0
    for i in range(up - 2, -1, -1):
        graph[i + 1][0] = graph[i][0]
    for i in range(down + 2, r):
        graph[i - 1][0] = graph[i][0]
    # 1. 맨 위와 맨 아래 row 순환
    for i in range(1, c):
        graph[0][i - 1] = graph[0][i]
        graph[r - 1][i - 1] = graph[r - 1][i]
    # 2. 가장 우측 위아래
    for i in range(0, up):
        graph[i][c - 1] = graph[i + 1][c - 1]
    for i in range(r - 1, down, -1):
        graph[i][c - 1] = graph[i - 1][c - 1]
    # 3. 공청기 우측
    for i in range(c - 1, 1, -1):
        graph[up][i] = graph[up][i - 1]
        graph[down][i] = graph[down][i - 1]
    graph[up][1], graph[down][1] = 0, 0
    return

airCirculator = findAirCirculator()
for _ in range(t):
    diffusion()
    operateAirCirculator(airCirculator[0], airCirculator[1])

for lst in graph:
    answer += sum(lst)
print(answer)
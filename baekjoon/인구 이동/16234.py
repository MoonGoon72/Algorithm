import sys
input = sys.stdin.readline

dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]

n, l, r = map(int, input().split())
data = list(list(map(int, input().split())) for _ in range(n))

def check(y, x):
    return 0 <= y < n and 0 <= x < n

def compare(a, b):
    return l <= abs(a - b) <= r

def flatten(civil, count):
    l = len(civil)
    num = count // l
    for y, x in civil:
        data[y][x] = num
    return

def bfs(r, c, visited):
    queue = [(r, c)]
    visited[r][c] = True
    idx = 0
    summation = 0
    while len(queue) > idx:
        y, x = queue[idx]
        idx += 1
        summation += data[y][x]
        for i in range(4):
            ny, nx = y + dy[i], x + dx[i]
            if check(ny, nx) and not visited[ny][nx] and compare(data[y][x], data[ny][nx]):
                queue.append((ny, nx))
                visited[ny][nx] = True
    return queue, summation

isMovable = True
answer = 0

while isMovable:
    civils = []
    isMovable = False
    visited = [[False] * n for _ in range(n)]
    for y in range(n):
        for x in range(n):
            if not visited[y][x]:
                civil, summation = bfs(y, x, visited)
                if len(civil) > 1:
                    civils.append((civil, summation))
                    isMovable = True
    if isMovable:
        for civil, summation in civils:
            flatten(civil, summation)
        answer += 1

print(answer)
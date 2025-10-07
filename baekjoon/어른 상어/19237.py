import sys
input = sys.stdin.readline

dy = [None, -1, 1, 0, 0]
dx = [None, 0, 0, -1, 1]

n, m, k = map(int, input().split())
graph = []
smell = [[(-1, -1)] * n  for _ in range(n)]
sharks = [(-1, -1) for _ in range(m + 1)]
priorities = [[[]] for _ in range(m + 1)]

for i in range(n):
    line = list(map(int, input().split()))
    for j in range(n):
        if line[j] != 0:
            sharks[line[j]] = (i, j)
            smell[i][j] = (k, line[j])
    graph.append(line)

direction = [0] + list(map(int, input().split()))

for s in range(1, m + 1):
    for d in range(1, 5):
        priority = list(map(int, input().split()))
        priorities[s].append(priority)

def check(y, x):
    return 0 <= y < n and 0 <= x < n

def shark_move():
    for s in range(1, m + 1):
        if sharks[s] == []:
            continue
        y, x = sharks[s]
        d = direction[s]
        candidates = []
        # 인접 빈 공간 찾기
        for i in range(1, 5):
            ny, nx = y + dy[i], x + dx[i]
            if check(ny, nx) and smell[ny][nx] == (-1, -1):
                candidates.append(i)
     
        if candidates:
            for p in priorities[s][d]:
                if p in candidates: # 빈 공간에 우선순위 높은걸 먼저 발견하니 이동 후 종료
                    ny, nx = y + dy[p], x + dx[p]
                    sharks[s] = (ny, nx)
                    direction[s] = p
                    break
        else: # 빈 공간이 없으면 냄새 있는 곳으로 되돌아가기
            for p in priorities[s][d]:
                ny, nx = y + dy[p], x + dx[p]
                if check(ny, nx) and smell[ny][nx][1] == s:
                    sharks[s] = (ny, nx)
                    direction[s] = p
                    break
    return

def smell_decrease():
    for i in range(n):
        for j in range(n):
            if smell[i][j] == (-1, -1): # 이거 좀 더 파이쏘닉하게
                continue
            nk, ns = smell[i][j]
            nk -= 1
            if nk == 0:
                smell[i][j] = (-1, -1)
                continue
            smell[i][j] = (nk, ns)

def shark_check():
    for s in range(m, 0, - 1):
        if sharks.count(sharks[s]) > 1:
            sharks[s] = (-1, -1)

def shark_smell():
    for s in range(1, m + 1):
        y, x = sharks[s]
        if (y, x) != (-1, -1):
            smell[y][x] = (k, s)

def is_done():
    for i in range(2, m + 1):
        if sharks[i] != (-1, -1):
            return False
    return True

time = 0
while not is_done():
    # 1. 상어 이동
    # 2. 냄새 감소
    # 3. 현재 상어 중복 체크
    # 4. 상어 냄새 추가
    time += 1
    if time > 1000:
        time = -1
        break
    
    shark_move()
    smell_decrease()
    shark_check()
    shark_smell()

print(time)
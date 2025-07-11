from collections import deque
import sys
input = sys.stdin.readline

dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]

walls = []
n, m = map(int, input().split())
data = [list(input().rstrip()) for _ in range(n)]
ids = [[0] * m for _ in range(n)]
size = [0]
cur_id = 0

def check(y, x):
    return 0 <= y < n and 0 <= x < m

for i in range(n):
    for j in range(m):
        if data[i][j] == '0' and ids[i][j] == 0:
            cur_id += 1
            queue = deque([(i, j)])
            count = 1
            ids[i][j] = cur_id
            while queue:
                y, x = queue.popleft()
                for d in range(4):
                    ny, nx = y + dy[d], x + dx[d]
                    if not check(ny, nx): continue
                    
                    if data[ny][nx] != '0' or ids[ny][nx] != 0: continue

                    ids[ny][nx] = cur_id
                    count += 1
                    queue.append((ny, nx))
            size.append(count)

ans = [['0'] * m for _ in range(n)]
for y in range(n):
    for x in range(m):
        if data[y][x] == '1':
            id_set = set()
            for d in range(4):
                ny, nx = y + dy[d], x + dx[d]
                if not check(ny, nx): continue

                id_set.add(ids[ny][nx])

            total = 1 + sum(size[i] for i in id_set)
            ans[y][x] = str(total % 10)

for row in ans:
    print(''.join(row))

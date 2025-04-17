from collections import deque
import sys
input = sys.stdin.readline

# 0 = 우, 1 = 하, 2 = 좌, 3 = 상
dy = [0, 1, 0, -1]
dx = [1, 0, -1, 0]

def check(y, x):
    return 1 <= y <= n and 1 <= x <= n

n = int(input())
k = int(input())
apple = list(tuple(map(int, input().split())) for _ in range(k))
l = int(input())
moves = deque(tuple(map(str, input().split())) for _ in range(l))

queue = deque()
y, x = 1, 1
d = 0
queue.append((y, x))
answer = 1

while True:
    y, x = queue[-1]
    ny, nx = y + dy[d], x + dx[d]
    if not check(ny, nx) or (ny, nx) in queue:
        print(answer)
        break
    queue.append((ny, nx))
    if len(moves) > 0 and answer == int(moves[0][0]):
        direction = moves.popleft()[1]
        if direction == "D":
            d = (d + 1) % 4
        else:
            d = d - 1 if d > 0 else 3
    answer += 1
    if (ny, nx) not in apple:
        queue.popleft()
    else:
        apple.remove((ny, nx))
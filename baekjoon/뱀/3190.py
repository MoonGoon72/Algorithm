from collections import deque
import sys
input = sys.stdin.readline

def check(y, x):
    return 1 <= y <= n and 1 <= x <= n

def rotate(d, info):
    if info == "D":
        d = (d + 1) % 4
    else:
        d = (d - 1) % 4
    return d

dy = [0, 1, 0, -1]
dx = [1, 0, -1, 0]

n = int(input())
board = [[0] * (n + 1) for _ in range(n + 1)]
k = int(input())

for _ in range(k):
    a, b = map(int, input().split())
    board[a][b] = 1

l = int(input())
moves = list(tuple(map(str, input().split())) for _ in range(l))

def solution():
    answer = 0
    y, x = 1, 1
    d = 0
    index = 0
    q = deque()
    q.append((y, x))

    while True:
        answer += 1
        ny, nx = y + dy[d], x + dx[d]
        if not check(ny, nx) or (ny, nx) in q:
            return answer
        q.append((ny, nx))
        # 사과 여부 체크
        if board[ny][nx] != 1:
            ty, tx = q.popleft()
            board[ty][tx] = 0
        board[ny][nx] = 2
        # 방향 전환 시간인지 체크
        if index < len(moves) and answer == int(moves[index][0]):
            d = rotate(d, moves[index][1])
            index += 1
        y, x = ny, nx

print(solution())

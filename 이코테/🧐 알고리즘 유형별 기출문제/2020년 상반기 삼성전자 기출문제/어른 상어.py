from collections import deque
import sys
input = sys.stdin.readline

dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]

n, m, k = map(int, input().split())
board = [[[] for _ in range(n)] for _ in range(n)]
smell_board = [[(0, 0)] * n for _ in range(n)]

sharks = [[] for _ in range(m + 1)] # index = 상어 number, [(y, x), d] 저장
priorities = [[] for _ in range(m + 1)]

for i in range(n):
    line = list(map(int, input().split()))
    for j in range(n):
        if line[j] != 0:
            sharks[line[j]] = [(i, j)]
            smell_board[i][j] = (k, line[j])
            board[i][j] = [line[j]]
    # board.append(line)

directions = list(map(int, input().split()))
for i in range(m):
    sharks[i + 1].append(directions[i] - 1) # sharks에는 [(좌표), 방향] 이 들어있게 됨

for i in range(1, m + 1): # 방향 별 우선 순위 저장
    for _ in range(4): # 상하좌우
        line = [int(x) - 1 for x in input().split()]
        priorities[i].append(line)

def check(y, x):
    return 0 <= y < n and 0 <= x < n

def is_alone():
    for i in range(2, m + 1):
        if sharks[i] != None:
            return False
    return True

def solution():
    answer = 0
    while True:
        answer += 1
        if answer > 1000:
            print(-1)
            return

        for shark in range(1, m + 1):
            if sharks[shark] == None:
                continue
            
            (y, x), d = sharks[shark]
            is_move = False
            for nd in priorities[shark][d]:
                ny, nx = y + dy[nd], x + dx[nd]
                if not check(ny, nx):
                    continue

                if smell_board[ny][nx] == (0, 0): # 이동 예정 장소로 갈 수 있으면 저장후 종료
                    sharks[shark] = [(ny, nx), nd]
                    board[ny][nx].append(shark)
                    board[y][x] = []
                    is_move = True
                    break
                
            if not is_move:
                for nd in priorities[shark][d]:
                    ny, nx = y + dy[nd], x + dx[nd]
                    if not check(ny, nx):
                        continue

                    if smell_board[ny][nx][1] == shark:
                        sharks[shark] = [(ny, nx), nd]
                        board[ny][nx].append(shark)
                        board[y][x] = []
                        break
        
        # 냄새 처리 및 상어 중복 제거
        for i in range(n):
            for j in range(n):
                # 냄새 처리
                if smell_board[i][j][0] > 1:
                    smell_board[i][j] = (smell_board[i][j][0] - 1, smell_board[i][j][1])
                else:
                    smell_board[i][j] = (0, 0)
                # 상어 중복 제거
                if len(board[i][j]) == 0:
                    continue
                elif len(board[i][j]) > 1:
                    for shark in board[i][j][1:]:
                        sharks[shark] = None
                smell_board[i][j] = (k, board[i][j][0])

        if is_alone():
            print(answer)
            return

solution()
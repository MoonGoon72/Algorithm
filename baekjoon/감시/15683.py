import sys, copy
input = sys.stdin.readline
# CCTV의 감시 방향은 정해져 있고, 회전 여부만을 통해 사각지대를 최소화 해야함.
# 백트래킹을 적용하는게 이런 문제를 푸는 데 보통 사용됨
# 회전하는 로직도 필요
# 회전 방향도 정해놔야 한다.
dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]
cctv = [[], 
        [[0], [1], [2], [3]],
        [[0, 1], [2, 3]],
        [[0, 3], [1, 2], [0, 2], [1, 3]],
        [[0, 1, 2], [0, 1, 3], [1, 2, 3], [0, 2, 3]],
        [[0, 1, 2, 3]]]

n, m = map(int, input().split())
board = []
cctvs = []

for r in range(n):
    line = list(map(int, input().split()))
    for c in range(m):
        if 0 < line[c] < 6:
            cctvs.append((r, c))
    board.append(line)

def check(y, x):
    return 0 <= y < n and 0 <= x < m

def calc(board):
    global answer
    cnt = 0
    for r in range(n):
        cnt += board[r].count(0)
    answer = min(answer, cnt)

def backtracking(cctvs, board):
    if not cctvs:
        calc(board)
        return
    r, c = cctvs[0]
    
    for directions in cctv[board[r][c]]:
        copied_board = copy.deepcopy(board)
        y, x = r, c
        for d in directions:
            ny, nx = y, x
            while True:        
                ny, nx = ny + dy[d], nx + dx[d]
                if not check(ny, nx):
                    break

                if copied_board[ny][nx] != 6:
                    if copied_board[ny][nx] == 0:
                        copied_board[ny][nx] = -1
                else:
                    break
        backtracking(cctvs[1:], copied_board)
answer = n * m

backtracking(cctvs, board)
print(answer)
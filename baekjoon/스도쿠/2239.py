import sys
input = sys.stdin.readline

board = []
# 1. row 전체 순회, 2. col 전체 순회, 3. 3x3 순회 후 안 뽑힌 수중 가장 작은 수를 선택
for i in range(9):
    row = list(map(int, input().strip()))
    board.append(row)
    
def backtracking(y, x):
    if y == 9:
        for row in board:
            print("".join(map(str, row)))
        exit(0)

    if board[y][x] != 0:
        next_x = (x + 1) % 9
        next_y = y + 1 if x == 8 else y
        backtracking(next_y, next_x)
        return
    
    possible_nums = set(range(1, 10))
    possible_nums -= set(board[y])
    possible_nums -= { board[i][x] for i in range(9) }
    y_start, x_start = (y // 3) * 3, (x // 3) * 3
    # 사각형 영역
    possible_nums -= { board[i][j] for i in range(y_start, y_start + 3) for j in range(x_start, x_start + 3)}
    
    for num in sorted(possible_nums):
        # 일단 시도
        board[y][x] = num
        # 다음 시도 하고 안되면 다음거
        next_x = (x + 1) % 9
        next_y = y + 1 if x == 8 else y
        backtracking(next_y, next_x)
        board[y][x] = 0

backtracking(0, 0)
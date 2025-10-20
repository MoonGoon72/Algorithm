import sys
input = sys.stdin.readline

board = []
empty = []

row_check = [set() for _ in range(9)]
col_check = [set() for _ in range(9)]
square_check = [[set() for _ in range(3)] for _ in range(3)]

for i in range(9):
    line = list(map(int, input().split()))
    for j in range(9):
        if line[j] == 0:
            empty.append((i, j))
        else:
            row_check[i].add(line[j])
            col_check[j].add(line[j])
            square_check[i // 3][j // 3].add(line[j])
    board.append(line)

def backtracking(idx):
    if idx == len(empty):
        for i in range(9):
            print(*board[i])
        exit(0)
        return
    
    y, x = empty[idx]
    possibles = set(range(1, 10))
    possibles -= row_check[y]
    possibles -= col_check[x]
    possibles -= square_check[y // 3][x // 3]

    for possible in possibles:
        board[y][x] = possible
        row_check[y].add(possible)
        col_check[x].add(possible)
        square_check[y // 3][x // 3].add(possible)
        backtracking(idx + 1)
        board[y][x] = 0
        row_check[y].remove(possible)
        col_check[x].remove(possible)
        square_check[y // 3][x // 3].remove(possible)

backtracking(0)
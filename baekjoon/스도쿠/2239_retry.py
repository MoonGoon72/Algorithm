import sys
input = sys.stdin.readline

board = []
row_check = [set() for _ in range(9)]
col_check = [set() for _ in range(9)]
square_check = [[set() for _ in range(3)] for _ in range(3)]
empty_cells = []

for i in range(9):
    row = list(map(int, input().strip()))
    board.append(row)
    for j in range(9):
        num = row[j]
        if num == 0:
            empty_cells.append((i, j))
        else:
            row_check[i].add(num)
            col_check[j].add(num)
            square_check[(i // 3)][(j // 3)].add(num)
def backtracking(index):
    if index == len(empty_cells):
        for i in range(9):
            print("".join(map(str, board[i])))
        exit(0)
    
    y, x = empty_cells[index]
    possible_nums = set(range(1, 10))
    possible_nums -= row_check[y]
    possible_nums -= col_check[x]
    possible_nums -= square_check[y // 3][x // 3]

    for num in sorted(possible_nums):
        board[y][x] = num
        row_check[y].add(num)
        col_check[x].add(num)
        square_check[y // 3][x // 3].add(num)
        backtracking(index + 1)
        board[y][x] = 0
        row_check[y].remove(num)
        col_check[x].remove(num)
        square_check[y // 3][x // 3].remove(num)

backtracking(0)
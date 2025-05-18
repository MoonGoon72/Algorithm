import sys
input = sys.stdin.readline

dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]

def is_hidable():
    for teacher in teachers:
        for i in range(4):
            y, x = teacher[0] + dy[i], teacher[1] + dx[i]
            while 0 <= y < n and 0 <= x < n:
                if board[y][x] == "S":
                    return False
                elif board[y][x] == "O" or board[y][x] == "T":
                    break
                y, x = y + dy[i], x + dx[i]
    return True

def backtracking(s):
    if len(walls) == 3:
        if is_hidable():
            print("YES")
            exit(0)
        else:
            return
    for i in range(s, len(empty)):
        walls.append(empty[i])
        board[empty[i][0]][empty[i][1]] = "O"
        backtracking(i + 1)
        walls.pop()
        board[empty[i][0]][empty[i][1]] = "X"

n = int(input())
board = []
teachers = []
empty = []
walls = []

for i in range(n):
    line = list(map(str, input().split()))
    for j in range(n):
        if line[j] == "T":
            teachers.append((i, j))
        elif line[j] == "X":
            empty.append((i, j))    
    board.append(line)

for i in range(len(empty) - 2):
    backtracking(i)

print("NO")
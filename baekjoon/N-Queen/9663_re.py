import sys
input = sys.stdin.readline
n = int(input())
answer = 0
board = [0] * n

def is_possible(x):
    for i in range(x):
        if board[i] == board[x] or abs(i - x) == abs(board[i] - board[x]):
            return False
    return True

def dfs(row):
    global answer
    if row == n:
        answer += 1
    else:
        for i in range(n):
            board[row] = i
            if is_possible(row):
                dfs(row+1)

dfs(0)
print(answer)
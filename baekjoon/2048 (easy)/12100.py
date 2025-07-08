import sys, copy
input = sys.stdin.readline

dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]

n = int(input())
board = list(list(map(int, input().split())) for _ in range(n))

def compose(board, d):
    if d == 0 or d == 1:  # 상하 움직임
        for i in range(n):
            line = [board[j][i] for j in range(n)]
            tiles = [x for x in line if x != 0]
            if d == 0:
                for j in range(len(tiles) - 1):
                    if tiles[j] != 0 and tiles[j] == tiles[j + 1]:
                        tiles[j] *= 2
                        tiles[j + 1] = 0
            else:
                for j in range(len(tiles) - 1, 0, -1):
                    if tiles[j] != 0 and tiles[j] == tiles[j - 1]:
                        tiles[j] *= 2
                        tiles[j - 1] = 0
            tmp = [x for x in tiles if x != 0]
            if d == 0:
                new_line = tmp + [0] * (n - len(tmp))
            else:
                new_line = [0] * (n - len(tmp)) + tmp
            for j in range(n):
                board[j][i] = new_line[j]
    else:  # 좌우 움직임
        for i in range(n):
            line = board[i]
            tiles = [x for x in line if x != 0]
            if d == 2:
                for j in range(len(tiles) - 1):
                    if tiles[j] != 0 and tiles[j] == tiles[j + 1]:
                        tiles[j] *= 2
                        tiles[j + 1] = 0
            else:
                for j in range(len(tiles) - 1, 0, -1):
                    if tiles[j] != 0 and tiles[j] == tiles[j - 1]:
                        tiles[j] *= 2
                        tiles[j - 1] = 0
            tmp = [x for x in tiles if x != 0]
            if d == 2:
                new_line = tmp + [0] * (n - len(tmp))
            else:
                new_line = [0] * (n - len(tmp)) + tmp
            board[i] = new_line
    return board

def move(board, time):
    global answer
    if time == 5:
        answer = max(answer, max(map(max, board)))
        return
    else:
        for d in range(4):
            new_board = compose(copy.deepcopy(board), d)
            move(new_board, time + 1)
    return

answer = 0
move(board, 0)
print(answer)
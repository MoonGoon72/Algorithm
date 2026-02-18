import sys
input = sys.stdin.readline

dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]

n = int(input())
data = [list(map(int, input().split())) for _ in range(n)]
answer = [0, 0, 0]

def papers(y, x, l):
    standard = data[y][x]
    for row in range(y, y+l):
        for col in range(x, x+l):
            if data[row][col] != standard:
                # 9등분
                nxt_l = l // 3
                for i in range(3):
                    for j in range(3):
                        papers(y + nxt_l * i, x + nxt_l * j, nxt_l)
                return
    answer[standard+1] += 1

papers(0, 0, n)
print("\n".join(map(str, answer)))
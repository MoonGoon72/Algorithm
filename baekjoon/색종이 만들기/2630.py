import sys
input = sys.stdin.readline

N = int(input())

graph= list(list(map(int, input().split())) for _ in range(N))
result = [0, 0]

def makePaper(y, x, n):
    color = graph[y][x]
    for row in range(n):
        for col in range(n):
            if graph[row + y][col + x] != color:
                makePaper(y, x, n // 2)
                makePaper(y + n // 2, x, n // 2)
                makePaper(y, x + n // 2, n // 2)
                makePaper(y + n // 2, x + n // 2, n // 2)
                return
    if color == 0:
        result[0] += 1
    else:
        result[1] += 1

makePaper(0, 0, N)

for answer in result:
    print(answer)


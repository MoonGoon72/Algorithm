import sys
N, col, row = map(int, input().split())

result = 0

while N != 0:
    N -= 1

    if col < 2 ** N and row < 2 ** N: #1사분면
        result += ((2 ** N) ** 2) * 0
    elif col < 2 ** N and row >= 2 ** N: #2사분면
        result += ((2 ** N) ** 2) * 1
        row -= (2 ** N)
    elif col >= 2 ** N and row < 2 ** N: #3사분면
        result += ((2 ** N) ** 2) * 2
        col -= (2 ** N)
    else: #4사분면
        result += ((2 ** N) ** 2) * 3
        row -= 2 ** N
        col -= 2 ** N

print(result)
import sys
input = sys.stdin.readline
N = int(input())
row = [0 for _ in range(N)]
result = 0

def is_promising(x):
    for i in range(x):
        if row[x] == row[i] or abs(row[x] - row[i]) == abs(x - i):
            return False
    return True

def dfs(x):
    global result
    if x == N:
        result += 1
    else:
        for i in range(N):
            row[x] = i
            if is_promising(x):
                dfs(x+1)

dfs(0)
print(result)
import sys
input = sys.stdin.readline

n = int(input())
matrix = [list(map(int, input().split())) for _ in range(n)]
p = [matrix[0][0]] + [matrix[i][1] for i in range(n)]
dp = [[0] * n for _ in range(n)]
for i in range(n):
    dp[i][i] = 0

for l in range(2, n + 1): # 부분 행렬 길이 2 ~ n
    for i in range(n - l + 1): # 시작 행렬 위치
        j = i + l - 1 # 끝 행렬 위치
        dp[i][j] = float('inf')
        for k in range(i, j):
            dp[i][j] = min(dp[i][j], dp[i][k] + dp[k + 1][j] + p[i] * p[k + 1] * p[j + 1])

print(dp[0][n-1])
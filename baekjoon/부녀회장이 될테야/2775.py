import sys
input = sys.stdin.readline
T = int(input())

for _ in range(T):
    k = int(input())
    n = int(input())
    dp = [x for x in range(1, n + 1)]


    for _ in range(k):
        for i in range(1, n):
            dp[i] += dp[i-1]
    print(dp[-1])

'''
3 | 1 5 15 35 70 ...
2 | 1 4 10 20 35 ...
1 | 1 3 6  10 15 ...
0 | 1 2 3  4  5 ...


k층 n호 => k층 n-1호 + k-1층 n호
dp[k][n-1] + dp[k-1][n] = dp[k][n]
''' 
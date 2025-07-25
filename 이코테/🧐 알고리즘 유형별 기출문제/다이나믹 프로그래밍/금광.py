t = int(input())

for _ in range(t):
    n, m = map(int, input().split())
    data = list(map(int, input().split()))
    
    dp = []
    index = 0
    for i in range(n):
        dp.append(data[index:index + m])
        index += m
    
    for j in range(1, m):
        for i in range(n):
            if i == 0:
                dp[i][j] = dp[i][j] + max(dp[i][j - 1], dp[i + 1][j])
            elif i == n - 1:
                dp[i][j] = dp[i][j] + max(dp[i - 1][j - 1], dp[i][j - 1])
            else:
                dp[i][j] = dp[i][j] + max(dp[i - 1][j - 1], dp[i][j - 1], dp[i + 1][j - 1])
    answer = 0
    for i in range(n):
        answer = max(answer, dp[i][m - 1])
    print(answer)
"""
2
3 4
1 3 3 2 2 1 4 1 0 6 4 7
4 4
1 3 1 5 2 2 4 1 5 0 2 3 0 6 1 2
"""
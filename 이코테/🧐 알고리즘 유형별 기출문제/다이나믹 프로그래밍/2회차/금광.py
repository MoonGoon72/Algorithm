t = int(input())

for _ in range(t):
    n, m = map(int, input().split())
    mine = []
    dp = [[0] * m for _ in range(n + 2)]

    data = list(map(int, input().split()))
    for i in range(n):
        line = data[m * i: m * (i + 1)]
        mine.append(line)
    
    for i in range(n):
        dp[i + 1][0] = mine[i][0]

    for i in range(1, m):
        for j in range(n):
            dp[j + 1][i] = max(dp[j + 1][i], max(dp[j][i - 1], dp[j + 1][i - 1], dp[j + 2][i - 1]) + mine[j][i])

    result = max(list(dp[i][m - 1] for i in range(n + 1)))
    print(result)

"""
2
3 4
1 3 3 2 2 1 4 1 0 6 4 7
4 4
1 3 1 5 2 2 4 1 5 0 2 3 0 6 1 2
"""
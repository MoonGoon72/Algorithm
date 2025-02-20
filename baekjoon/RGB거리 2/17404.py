import sys
input = sys.stdin.readline

n = int(input())
costs = list(list(map(int, input().split())) for _ in range(n))
INF = int(1e9)
answer = INF

for first_color in range(3):
    dp = [[INF] * 3 for _ in range(n)]
    
    dp[0][first_color] = costs[0][first_color]

    for i in range(1, n):
        dp[i][0] = min(dp[i - 1][1], dp[i - 1][2]) + costs[i][0]
        dp[i][1] = min(dp[i - 1][0], dp[i - 1][2]) + costs[i][1]
        dp[i][2] = min(dp[i - 1][0], dp[i - 1][1]) + costs[i][2]    

    for last_color in range(3):
        if first_color != last_color:
            answer = min(answer, dp[n - 1][last_color])

print(answer)
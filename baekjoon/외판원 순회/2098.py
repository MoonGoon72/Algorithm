import sys
input = sys.stdin.readline

inf = int(1e9)
n = int(input())
cost = [list(map(int, input().split())) for _ in range(n)]
dp = [[inf] * n for _ in range(1 << n)]
dp[1 << 0][0] = 0 # 0번 도시 방문

for mask in range(1 << n):
    for cur in range(n):
        if not (mask & (1 << cur)): continue
        for nxt in range(n):
            # 아직 방문을 안 한 상태이고, cost도 존재하여 이동 가능
            if (mask & (1 << nxt) == 0 and cost[cur][nxt]):
                next_mask = mask | (1 << nxt)
                dp[next_mask][nxt] = min(dp[next_mask][nxt], dp[mask][cur] + cost[cur][nxt])

answer = inf
full = (1 << n) - 1
for i in range(n):
    if cost[i][0] != 0: # 0번 도시로 돌아올 수 있음
        answer = min(answer, dp[full][i] + cost[i][0])
print(answer)
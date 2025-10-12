import sys
input = sys.stdin.readline

INF = int(1e9)
n = int(input())
graph = [[] for _ in range(n)]

for i in range(n):
    line = list(map(int, input().split()))
    graph[i] = line

dp = [[-1] * (1 << n) for _ in range(n)]

def tsp(cur, mask):
    if mask == (1 << n) - 1:
        return graph[cur][0] if graph[cur][0] > 0 else INF
    if dp[cur][mask] != -1:
        return dp[cur][mask]
    
    best = INF
    for nxt in range(n):
        if (1 << nxt) & mask:
            continue
        if graph[cur][nxt] != 0:
            best = min(best, graph[cur][nxt] + tsp(nxt, mask | (1 << nxt)))
    dp[cur][mask] = best
    return dp[cur][mask]

answer = tsp(0, 1 << 0)
print(answer)

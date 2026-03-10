from collections import deque
import sys
input = sys.stdin.readline
INF = int(1e9)
# F: 꼭대기, S: 현 위치, G: 목표, U: 위로 이동 층 수, D: 아래로 이동 층 수
f, s, g, u, d = map(int, input().split())
dp = [INF] * (f+1)
dp[s] = 0

queue = deque()
queue.append((s, 0))
while queue:
    now, cost = queue.popleft()
    if dp[now] < cost: continue
    # 위
    if now + u <= f and cost + 1 < dp[now + u]:
        dp[now + u] = cost + 1
        queue.append((now + u, cost + 1))
    # 아래
    if now - d >= 1 and cost + 1 < dp[now - d]:
        dp[now - d] = cost + 1
        queue.append((now - d, cost + 1))

print(dp[g] if dp[g] != INF else 'use the stairs')
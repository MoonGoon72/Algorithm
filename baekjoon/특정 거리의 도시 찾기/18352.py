import sys
input = sys.stdin.readline

n, m, k, x = map(int, input().split())
road = list(0 for _ in range(n + 1))
visited = list(False for _ in range(n + 1))
# 거리정보 저장
for _ in range(m):
    a, b = map(int, input().split())
    road[a].append(b)

for i in range(1,k+1):
    road[x]
    if (not visited[i]):


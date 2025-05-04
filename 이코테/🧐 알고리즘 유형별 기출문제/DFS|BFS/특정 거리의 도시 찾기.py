import sys, heapq
input = sys.stdin.readline

INF = int(1e9)
n, m, k, x = map(int, input().split())
graph = [[] for _ in range(n + 1)]
distance = [INF] * (n + 1)

distance[x] = 0

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)

queue = []
heapq.heappush(queue, (0, x))

while queue:
    dist, now = heapq.heappop(queue)
    if dist > distance[now]:
        continue
    
    for node in graph[now]:
        if distance[node] > dist + 1:
            distance[node] = dist + 1
            heapq.heappush(queue, (distance[node], node))

if k not in distance:
    print(-1)
    exit(0)

for (i, e) in enumerate(distance):
    if e == k:
        print(i)
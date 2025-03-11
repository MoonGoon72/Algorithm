import sys, heapq
input = sys.stdin.readline
INF = int(1e9)

def dijkstra(start):
    visited = [False] * (n + 1)
    distance = [INF] * (n + 1)
    distance[start] = 0
    visited[start] = True
    queue = []
    heapq.heappush(queue, (0, start))
    
    while queue:
        dist, now = heapq.heappop(queue)
        if distance[now] < dist:  # 갱신 된거면 탐색 안함
            continue
        
        for (node, l) in graph[now]:
            cost = dist + l
            if not visited[node]:
                distance[node] = cost
                visited[node] = True
                heapq.heappush(queue, (distance[node], node))
            else:
                if distance[node] < cost:
                    continue
                else:
                    distance[node] = cost
                    heapq.heappush(queue, (cost, node))
    answer = 0
    for i in range(1, n + 1):
        if distance[i] <= m:
            answer += items[i]
    return answer

n, m, r = map(int, input().split())
items = [0] + list(map(int, input().split()))
graph = [[] for _ in range(n + 1)]

for _ in range(r):
    a, b, l = map(int, input().split())
    graph[a].append((b, l))
    graph[b].append((a, l))

answer = dijkstra(1)
for i in range(2, n + 1):
    tmp = dijkstra(i)
    answer = max(answer, tmp)
print(answer)
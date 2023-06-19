import heapq
import sys
input = sys.stdin.readline

V, E = map(int, input().split(' '))
K = int(input())
INF = float('infinity')
graph = [[] for _ in range(V + 1)]
distance = [INF for _ in range(V + 1)]
distance[K] = 0

for _ in range(E):
    u, v, w = map(int, input().split(' '))
    graph[u].append((v, w))



def dijkstra(start):
    queue = []
    heapq.heappush(queue, (distance[start], start))

    while queue:
        now_distance, now = heapq.heappop(queue)

        # heap에 넣은 시점보다 현재 시점의 distance가 짧은 경우 탐색하지 않아야 함

        if now_distance > distance[now]: continue

        for (node, n_weight) in graph[now]:
            if distance[node] > now_distance + n_weight:
                distance[node] = now_distance + n_weight
                heapq.heappush(queue, (distance[node], node))

dijkstra(K)
for i in range(1, V + 1):
    if distance[i] == INF:
        print("INF")
    else:
        print(distance[i])

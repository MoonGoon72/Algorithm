import sys
import heapq
input = sys.stdin.readline

INF = float('infinity')
N = int(input())
M = int(input())

costs = [INF for _ in range(N + 1)]

graph = [[] for _ in range(N+1)]

for _ in range(M):
    u, v, c = map(int, input().split(' '))
    graph[u].append((v, c))

start, end = map(int, input().split(' '))
costs[start] = 0

def dijkstra(start):
    queue = []

    heapq.heappush(queue, (costs[start], start))
    while queue:
        n_cost, now = heapq.heappop(queue)

        if n_cost > costs[now]: continue

        for node, cost in graph[now]:
            if costs[node] > cost + costs[now]:
                costs[node] = cost + costs[now]
                heapq.heappush(queue, (costs[node], node))

dijkstra(start)

print(costs[end])

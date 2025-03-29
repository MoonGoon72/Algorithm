import sys, heapq
input = sys.stdin.readline
INF = int(1e9)

n, m, c = map(int, input().split())

def floyd():
    distance = [[INF] * (n + 1) for _ in range(n + 1)]

    for _ in range(m):
        x, y, z = map(int, input().split())
        distance[x][y] = z

    for i in range(1, n + 1):
        distance[i][i] = 0

    for i in range(1, n + 1):
        for j in range(1, n + 1):
            for k in range(1, n + 1):
                distance[i][j] = min(distance[i][j], distance[i][k] + distance[k][j])

    cities = 0
    answer = 0
    for i in range(1, n + 1):
        if distance[c][i] != INF and i != c:
            cities += 1
            answer = max(answer, distance[c][i])
    return ((cities, answer))

def dijkstra():
    graph = [[] for _ in range(n + 1)]
    
    for _ in range(m):
        x, y, z = map(int, input().split())
        graph[x].append((y, z))

    distance = [INF] * (n + 1)
    distance[c] = 0
    queue = []
    heapq.heappush(queue, (0, c))
    
    while queue:
        dist, now = heapq.heappop(queue)
        if distance[now] < dist:
            continue
        
        for node, cost in graph[now]:
            tmp = dist + cost
            if distance[node] > tmp:
                distance[node] = tmp
                heapq.heappush(queue, (tmp, node))
    
    cities = 0
    answer = 0
    for i in range(1, n + 1):
        if i != c and distance[i] != INF:
            cities += 1
            answer = max(answer, distance[i])
    return (cities, answer)

# print(*floyd())
print(*dijkstra())
"""
3 2 1
1 2 4
1 3 2

2 4
"""
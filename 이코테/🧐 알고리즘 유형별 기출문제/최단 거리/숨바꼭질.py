import sys, heapq
input = sys.stdin.readline

inf = int(1e9)
n, m = map(int, input().split())
board = [[] for _ in range(n + 1)]

for _ in range(m):
    a, b = map(int, input().split())
    board[a].append(b)
    board[b].append(a)

def dijkstra(num):
    distance = [inf] * (n + 1)
    distance[num] = 0
    queue = [(0, num)]

    while queue:
        cost, now = heapq.heappop(queue)
        if distance[now] > cost:
            continue
        
        for next_node in board[now]:
            next_cost = cost + 1
            if distance[next_node] > next_cost:
                distance[next_node] = next_cost
                heapq.heappush(queue, (next_cost, next_node))
    
    answer_distance = 0
    barns = []
    for barn in range(1, n + 1):
        if answer_distance < distance[barn]:
            barns = [barn]
            answer_distance = distance[barn]
        elif answer_distance == distance[barn]:
            barns.append(barn)
    return barns[0], answer_distance, len(barns)

a, b, c = dijkstra(1)
print(a, b, c)
"""
6 7
3 6
4 3
3 2
1 3
1 2
2 4
5 2
--- result ---
4 2 3
"""

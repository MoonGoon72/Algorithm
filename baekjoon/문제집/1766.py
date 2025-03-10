import sys, heapq
input = sys.stdin.readline

n, m = map(int, input().split())
graph = [[] for _ in range(n + 1)]
in_degree = [0] * (n + 1)

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    in_degree[b] += 1

queue = []
answer = []
for i in range(1, n + 1):
    if in_degree[i] == 0:
        queue.append(i)

while queue:
    now = heapq.heappop(queue)
    answer.append(now)
    for node in graph[now]:
        in_degree[node] -= 1
        if in_degree[node] == 0:
            heapq.heappush(queue, node)

print(*answer)
from collections import deque
import sys
input = sys.stdin.readline

t = int(input())

for _ in range(t):
    n, k = map(int, input().split())
    weights = [0] + list(map(int, input().split()))
    graph = [[] for _ in range(n + 1)]
    times = [0] * (n + 1)
    indegree = [0] * (n + 1)
    
    for _ in range(k):
        x, y = map(int, input().split())
        graph[x].append(y)
        indegree[y] += 1
    w = int(input())

    def topology_sort():
        queue = deque()
        for i in range(1, n + 1):
            if indegree[i] == 0:
                queue.append(i)

        while queue:
            now = queue.popleft()
            if now == w:
                return times[now] + weights[now]
            while graph[now]:
                node = graph[now].pop()
                times[node] = max(times[node], times[now] + weights[now])
                indegree[node] -= 1
                if indegree[node] == 0:
                    queue.append(node)
        return

    print(topology_sort())
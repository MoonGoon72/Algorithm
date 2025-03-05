from collections import deque
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
graph = [[] for _ in range(n + 1)]
in_degree = [0] * (n + 1)
out_degree = [0] * (n + 1)
answer = []

for _ in range(m):
    arr = list(map(int, input().split()))
    num = arr[0]
    for i in range(1, num):
        graph[arr[i]].append(arr[i + 1])
        in_degree[arr[i + 1]] += 1
        out_degree[arr[i]] += 1

queue = deque()
for i in range(1, n + 1):
    if in_degree[i] == 0:
        queue.append(i)

while queue:
    now = queue.popleft()
    answer.append(now)
    for node in graph[now]:
        in_degree[node] -= 1
        out_degree[now] -= 1
        if in_degree[node] == 0:
            queue.append(node)

if len(list(filter(lambda x: x > 0, in_degree))) > 0:
    print(0)
else:
    print("\n".join(map(str, answer)))
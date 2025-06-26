from collections import deque
import sys
input = sys.stdin.readline

t = int(input())

for _ in range(t):
    n = int(input())
    past_scores = list(map(int, input().split()))
    m = int(input())
    changed = list(map(int, input().split()) for _ in range(m))
    in_degree = [0] * (n + 1)

    graph = [[] for _ in range(n + 1)]
    for i in range(n - 1):
        for j in range(i + 1, n):
            in_degree[past_scores[j]] += 1
            graph[past_scores[i]].append(past_scores[j])

    for change in changed:
        a, b = change
        if b in graph[a]: # a < b -> b < a
            in_degree[b] -= 1
            in_degree[a] += 1
            graph[a].remove(b)
            graph[b].append(a)
        else:
            in_degree[a] -= 1
            in_degree[b] += 1
            graph[b].remove(a)
            graph[a].append(b)
        
    queue = deque()    
    for i in range(1, n + 1):
        if in_degree[i] == 0:
            queue.append(i)

    answer = []
    while queue:
        now = queue.popleft()
        answer.append(now)
        
        for next_node in graph[now]:
            in_degree[next_node] -= 1
            if in_degree[next_node] == 0:
                queue.append(next_node)
    
    if len(answer) != n:
        print("IMPOSSIBLE")
    else:
        print(*answer)
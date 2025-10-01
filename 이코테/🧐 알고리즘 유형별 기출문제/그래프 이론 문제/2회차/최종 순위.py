from collections import deque
import sys
input = sys.stdin.readline

t = int(input())

for _ in range(t):
    n = int(input())
    prev = list(map(int, input().split()))
    m = int(input())
    in_degree = [0] * (n + 1)
    is_impossible = False

    graph = [[False] * (n + 1) for _ in range(n + 1)]
    for i in range(n - 1):
        v1 = prev[i]
        for j in range(i + 1, n):
            v2 = prev[j]
            in_degree[v2] += 1
            graph[v1][v2] = True
    
    for _ in range(m):
        a, b = map(int, input().split())
        if is_impossible:
            continue
        if graph[a][b] == True:
            in_degree[b] -= 1
            in_degree[a] += 1
            if in_degree[b] < 0:
                is_impossible = True
                continue
            graph[a][b] = False
            graph[b][a] = True        
        elif graph[b][a] == True:
            in_degree[a] -= 1
            in_degree[b] += 1
            if in_degree[a] < 0:
                is_impossible = True
                continue
            graph[b][a] = False
            graph[a][b] = True

    if is_impossible:
        print("IMPOSSIBLE")
        break

    queue = deque()
    for i in range(1, n + 1):
        if in_degree[i] == 0:
            queue.append(i)
    
    answer = []
    while queue:
        if len(queue) != 1:
            print("?")
            break
        now = queue.popleft()
        answer.append(now)
        for i in range(1, n + 1):
            if graph[now][i] == True:
                graph[now][i] = False
                in_degree[i] -= 1
                if in_degree[i] == 0:
                    queue.append(i)
    
    if len(answer) == n:
        print(*answer)
    else:
        print("IMPOSSIBLE")
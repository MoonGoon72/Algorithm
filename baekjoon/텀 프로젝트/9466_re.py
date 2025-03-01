import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

def dfs(node):
    global cycle_count
    visited[node] = 1
    next_node = graph[node]
    tmp = next_node

    if visited[next_node] == 0:
        dfs(next_node)
    elif visited[next_node] == 1:
        while True:
            cycle_count += 1
            tmp = graph[tmp]
            if tmp == next_node:
                break
    visited[node] = 2
    return

t = int(input())

for _ in range(t):
    n = int(input())
    graph = [0] + list(map(int, input().split()))
    visited = [0] * (n + 1)
    cycle_count = 0

    for i in range(1, n + 1):
        if visited[i] == 0:
            dfs(i)
    print(n - cycle_count)
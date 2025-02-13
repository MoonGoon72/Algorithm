import sys
sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline

n, r, q = map(int, input().split())
graph = [[] for _ in range(n + 1)]
dp = [0] * (n + 1)

for _ in range(n - 1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

def get_vertex(parent, node):
    if graph[node].count == 1:
        if dp[node] == 0: 
            dp[node] = 1
        return 1
    tmp = 0
    for child in graph[node]:
        if child != parent:
            tmp += get_vertex(node, child)
    if dp[node] == 0:
        dp[node] = tmp + 1
    return tmp + 1

get_vertex(0, r)
for _ in range(q):
    query = int(input())
    print(dp[query])

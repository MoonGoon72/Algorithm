from collections import deque
import sys
input = sys.stdin.readline

t = int(input())

def binary_graph():
    v, e = map(int, input().split())
    graph = [[] for _ in range(v + 1)]
    
    for _ in range(e):
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)
    
    nodes = [0] * (v + 1)
    
    for node in range(1, v + 1):
        if nodes[node] == 0:
            queue = deque()
            queue.append(node)
            nodes[node] = -1
            
            while queue:
                now = queue.popleft()
                for node in graph[now]:
                    if nodes[node] == 0:
                        nodes[node] = nodes[now] * -1
                        queue.append(node)
                    elif nodes[node] == nodes[now] * -1:
                        continue
                    else:
                        print("NO")
                        return
    print("YES")
    return

for _ in range(t):
    binary_graph()

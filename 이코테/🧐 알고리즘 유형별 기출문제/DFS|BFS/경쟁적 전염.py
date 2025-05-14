from collections import defaultdict
import sys
input = sys.stdin.readline

dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]

def check(y, x):
    return 0 <= y < n and 0 <= x < n

n, k = map(int, input().split())
graph = []
dict = defaultdict(list)
for i in range(n):
    line = list(map(int, input().split()))
    for j in range(n):
        if line[j] != 0:
            dict[line[j]].append((i, j))
    graph.append(line)

s, sy, sx = map(int, input().split())

for _ in range(s):
    for i in range(1, k + 1):
        tmp = list()
        while dict[i]: 
            y, x = dict[i].pop()
            for j in range(4):
                ny, nx = y + dy[j], x + dx[j]
                if check(ny, nx) and graph[ny][nx] == 0:
                    graph[ny][nx] = i
                    tmp.append((ny, nx))
        dict[i] = tmp

print(graph[sy - 1][sx - 1])
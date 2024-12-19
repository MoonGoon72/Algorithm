from collections import deque
import sys
input = sys.stdin.readline

dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]

n = int(input())
graph = [list(map(str, input().rstrip())) for _ in range(n)]

def check(y, x):
    return 0 <= y < n and 0 <= x < n

def bfs(isBlind: bool):
    visited = [[False for _ in range(n)] for _ in range(n)]
    queue = deque()
    count = 0

    for y in range(n):
        for x in range(n):
            queue.append((y, x))
            isChanged = False

            while queue:
                (ry, rx) = queue.popleft()
                if check(ry, rx) and not visited[ry][rx]:
                    visited[ry][rx] = True
                    isChanged = True
                    nowColor = graph[ry][rx]

                    for i in range(4):
                        ny = ry + dy[i]
                        nx = rx + dx[i]
                        
                        if check(ny, nx) and not visited[ny][nx]:
                            nextColor = graph[ny][nx]
                            if nextColor == nowColor:
                                queue.append((ny, nx))
                            else:
                                if isBlind:
                                    if nextColor != "B" and nowColor != "B":
                                        queue.append((ny, nx))
            if isChanged:
                count += 1
    return count

print(bfs(False), bfs(True))

from collections import deque
import sys
input = sys.stdin.readline

n = int(input())
r1, c1, r2, c2 = map(int, input().rstrip().split())
moves = [(-2, -1), (-2, 1), (0, -2), (0, 2), (2, -1), (2, 1)]

def check(y, x):
    return 0 <= y < n and 0 <= x < n

def bfs(r, c):
    visited = set()    
    visited.add((r, c))
    queue = deque([(r, c, 0)])
    while queue:
        y, x, depth = queue.popleft()
        for dy, dx in moves:
            ny, nx = y + dy, x + dx
            if not check(ny, nx) or (ny, nx) in visited: continue

            if (ny, nx) == (r2, c2):
                return depth + 1
            queue.append((ny, nx, depth + 1))
            visited.add((ny, nx))
    return -1

answer = bfs(r1, c1)
print(answer)
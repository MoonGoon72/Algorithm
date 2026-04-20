import sys
input = sys.stdin.readline

n, k, m = map(int, input().split())
graph = [0 for _ in range(k+1)]
students = list(map(int, input().split()))
recommended_videos = list(map(int, input().split()))

LOG = 30
jump = [[0] * LOG for _ in range(k + 1)]
for v in range(k):
    jump[v+1][0] = recommended_videos[v]
for j in range(1, LOG):
    for v in range(1, k+1):
        jump[v][j] = jump[jump[v][j-1]][j-1]

steps = m - 1
for i in range(n):
    cur = students[i]
    for j in range(LOG):
        if steps & (1 << j):
            cur = jump[cur][j]
    students[i] = cur

print(*students)

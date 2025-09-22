n, m = map(int, input().split())
inf = int(1e9)
distance = [[inf] * (n + 1) for _ in range(n + 1)]

for i in range(1, n + 1):
    distance[i][i] = 0

for _ in range(m):
    a, b = map(int, input().split())
    distance[a][b] = 1

for k in range(1, n + 1):
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            distance[i][j] = min(distance[i][j], distance[i][k] + distance[k][j])

answer = 0
for i in range(1, n + 1):
    count = 0
    for j in range(1, n + 1):
        if distance[i][j] != inf or distance[j][i] != inf:
            count += 1
    if count == n:
        answer += 1

print(answer)

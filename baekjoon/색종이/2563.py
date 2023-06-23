n = int(input())


graph = [[0 for _ in range(100)] for _ in range(100)]
result = 0
for _ in range(n):
    x, y = map(int, input().split(' '))
    for i in range(x, x + 10):
        for j in range(y, y + 10):
            graph[i][j] = 1

for i in range(100):
    result += sum(graph[i])
print(result)
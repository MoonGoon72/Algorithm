import sys
input = sys.stdin.readline

n, m = map(int, input().split())
matrix = list(list(map(int, input().split())) for _ in range(n))

result = 0
for row in matrix:
    result = max(result, min(row))
print(result)
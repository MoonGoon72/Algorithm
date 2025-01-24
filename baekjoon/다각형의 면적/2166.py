from decimal import *
import sys
input = sys.stdin.readline

n = int(input())
points = [list(map(int, input().split())) for _ in range(n)]
area = 0

for i in range(n - 1):
    x1, y1 = points[i]
    x2, y2 = points[i + 1]
    area += x1 * y2 - x2 * y1
x1, y1 = points[-1]
x2, y2 = points[0]
area += x1 * y2 - x2 * y1
area = abs(area) / 2

result = round(area + 0.0000000001, 2)
print(result)
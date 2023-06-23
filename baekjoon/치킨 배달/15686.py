import sys
input = sys.stdin.readline
import copy
from itertools import combinations

n, m = map(int, input().split(' '))
graph = [list(map(int, input().split(' '))) for _ in range(n)]
houses = []
chicken_houses = []
result = 10000000

for i in range(n):
        for j in range(n):
            if graph[i][j] == 2:
                chicken_houses.append((i, j))
            elif graph[i][j] == 1:
                houses.append((i, j))


for chicken in combinations(chicken_houses, m):
    cnt = 0
    for a, b in houses:
        tmp = 101
        for c, d in chicken:
            tmp = min(tmp, abs(c - a) + abs(d - b))
        cnt += tmp
    result = min(cnt, result)
print(result)

# def select_chicken(num, chicken_house):
#     if num == m:
#         chicken_distance(chicken_house)
#         return
#     else:
#         for chicken in chicken_houses:
#             chicken_house.append(chicken)
#             select_chicken(num+1, chicken_house)
#             chicken_house.pop()


# def chicken_distance(chicken_house):
#     global result
#     cnt = 0
#     for a, b in houses:
#         tmp = 101
#         for c, d in chicken_house:
#             tmp = min(tmp, abs(c - a) + abs(d - b))
#         cnt += tmp
#     result = min(cnt, result)

# select_chicken(0, [])
# print(result)
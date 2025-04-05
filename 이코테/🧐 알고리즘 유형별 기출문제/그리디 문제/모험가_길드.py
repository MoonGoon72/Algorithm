import sys
input = sys.stdin.readline

n = int(input())
data = list(map(int, input().split()))
data.sort()

count = 0
answer = 0

for i in data:
    count += 1
    if count >= i:
        answer += 1
        count = 0
print(answer)

"""
5
2 3 1 2 2

2
"""
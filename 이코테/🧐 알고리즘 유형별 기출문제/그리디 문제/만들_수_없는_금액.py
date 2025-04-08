n = int(input())
data = list(map(int, input().split()))
data.sort()

target = 1
for c in data:
    if target < c:
        break
    target += c

print(target)

"""
5
3 2 1 1 9

8
"""
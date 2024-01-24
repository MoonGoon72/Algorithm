import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))

tmp = sorted(list(set(arr)))
dict = {}

for i, x in enumerate(tmp):
    dict[x] = i

result = []

for j in arr:
    result.append(str(dict[j]))

print(' '.join(result))

import sys
input = sys.stdin.readline

n, m = map(int, input().split())
accumulates = [0]
nums = list(map(int, input().split()))
num = 0
for n in nums:
    num += n
    accumulates.append(num)

for _ in range(m):
    i, j = map(int, input().split())
    result = accumulates[j] - accumulates[i-1]
    print(result)

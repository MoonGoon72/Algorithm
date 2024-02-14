import sys
input = sys.stdin.readline

n, m = map(int, input().split())
sets = 100000000
single = 100000000

sets_arr = []
single_arr = []

for _ in range(m):
    a, b = map(int, input().split())
    sets_arr.append(a)
    single_arr.append(b)

provider = n // 6
divider = n % 6

sets_min = min(sets_arr)
single_min = min(single_arr)

provider_min = min(sets_min, single_min * 6)

if sets_min < single_min * divider:
    result = (provider + 1) * provider_min
else:
    result = provider * provider_min + single_min * divider
print(result)
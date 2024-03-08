import copy
n = int(input())
a = list(map(int, input().split()))

memoization = copy.deepcopy(a)

for i in range(1, n):
    memoization[i] = max(memoization[i], memoization[i -1] + memoization[i])

print(max(memoization))
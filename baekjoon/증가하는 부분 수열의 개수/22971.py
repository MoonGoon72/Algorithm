import sys
input = sys.stdin.readline
MOD = 998_244_353
n = int(input())
data = [0] + list(map(int, input().rstrip().split()))
lis = [0] + [1] * (n)

for i in range(1, n+1):
    for j in range(i):
        if data[j] < data[i]:
            lis[i] += lis[j]
            lis[i] %= MOD
print(*lis[1:])

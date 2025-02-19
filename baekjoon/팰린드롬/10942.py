import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

n = int(input())
numbers = [0] + list(map(int, input().split()))
m = int(input())
dp = [[0] * (n + 1) for _ in range(n + 1)]

for i in range(1, n + 1):
    dp[i][i] = 1
for i in range(1, n):
    if numbers[i] == numbers[i + 1]:
        dp[i][i + 1] = 1
for length in range(2, n):
    for s in range(1, n - length + 1):
        e = s + length
        if numbers[s] == numbers[e] and dp[s + 1][e - 1] == 1:
            dp[s][e] = 1
for _ in range(m):
    s, e = map(int, input().split())
    print(1 if dp[s][e] else 0)
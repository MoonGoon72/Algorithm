import sys
input = sys.stdin.readline

t = int(input())
array = []
for _ in range(t):
    array.append(int(input()))

dp = [1] * 10001

for i in range(2, 10001):
    dp[i] += dp[i - 2]

for i in range(3, 10001):
    dp[i] += dp[i - 3]

for num in array:
    print(dp[num])
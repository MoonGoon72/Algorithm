import sys
input = sys.stdin.readline

n, k = map(int, input().split())
coins = list(int(input()) for _ in range(n))
# n 개의 코인을 중복해서 사용하여 k를 만드는 경우 중 코인을 가장 조금 쓸 때의 최소 갯수
dp = [int(1e9)] * 10_001
for coin in coins:
    if coin <= k:
        dp[coin] = 1

for i in range(1, k+1):
    for coin in coins:
        summation = coin + i
        if summation > k: continue

        dp[summation] = min(dp[summation], dp[i] + 1)
print(dp[k] if dp[k] != int(1e9) else -1)
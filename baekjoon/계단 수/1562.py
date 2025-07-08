import sys
input = sys.stdin.readline

mod = 1_000_000_000
n = int(input())
# 3차원 배열 dp[i][j][mask]
# i = 현재 수의 길이, 
# j = 현재 수의 마지막 수, 
# mask = 사용한 수의 비트 값
dp = [[[0] * (1 << 10) for _ in range(10)] for _ in range(n + 1)]
for i in range(1, 10):
    dp[1][i][1 << i] = 1

if n < 10:
    print(0)
    exit(0)

for i in range(1, n): # 자리 수
    for j in range(10): # 마지막 수
        for mask in range(1 << 10):
            if dp[i][j][mask] == 0: continue

            if j > 0:
                nxt = j - 1
                next_mask = mask | (1 << nxt)
                dp[i + 1][nxt][next_mask] = (dp[i + 1][nxt][next_mask] + dp[i][j][mask]) % mod
            
            if j < 9:
                nxt = j + 1
                next_mask = mask | (1 << nxt)
                dp[i + 1][nxt][next_mask] = (dp[i + 1][nxt][next_mask] + dp[i][j][mask]) % mod
            
full_mask = (1 << 10) - 1 # shift 연산은 산술 연산보다 우선순위가 떨어짐 그래서 괄호 필요함
answer = 0
for i in range(10):
    answer = (answer + dp[n][i][full_mask]) % mod
print(answer)

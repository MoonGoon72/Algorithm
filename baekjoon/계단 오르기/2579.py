import sys
input = sys.stdin.readline
N = int(input())
stairs = []
dp = [0 for _ in range(N)]
for _ in range(N):
    stairs.append(int(input()))

if N <= 2:
    print(sum(stairs))
else:
    dp[0] = stairs[0]
    dp[1] = stairs[0] + stairs[1]
    for i in range(2, N):
        dp[i] = max(dp[i-3] + stairs[i-1] + stairs[i], dp[i-2] + stairs[i])

    print(dp[-1])

'''
규칙
한번에 하나 혹은 두 계단
연속해서 3개 계단 불가능
마지막 계단은 밟아야함
dp 배열을 특정 계단일 때 최대값으로 하자
'''

'''
10 20 15 15 10 20
dp[0] = 10
dp[1] = 10 + 20 = 30
dp[2] = 10 + 15 or 20 + 15 / dp[0] + s[2] or dp[-1] + s[1] + s[2]
dp[3] = dp[0] + stair[2] + 4 = 8 / dp[]
'''
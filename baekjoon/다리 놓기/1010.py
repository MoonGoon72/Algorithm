import math

T = int(input())
for _ in range(T):
    N, M = map(int, input().split(' '))
    # bridge = math.factorial(M) // (math.factorial(N) * math.factorial(M-N))
    # print(bridge)


def bridge(n, m):
    dp = [[0 for _ in range(m + 1)] for _ in range(n+1)]

    for i in range(1, m+1):
        dp[1][i] = i
    
    for j in range(2, n+1):
        for k in range(j, m+1):
            for l in range(k, j-1, -1):


'''
N 개 M 개 사이트 존재하고
다리는 교차 불가능 
N개 기준으로 해야함

'''
import math

T = int(input())
for _ in range(T):
    N, M = map(int, input().split(' '))
    bridge = math.factorial(M) // (math.factorial(N) * math.factorial(M-N))
    print(bridge)

'''
N 개 M 개 사이트 존재하고
다리는 교차 불가능 
N개 기준으로 해야함

'''